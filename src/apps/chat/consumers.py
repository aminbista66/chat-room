from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .utils import get_user
import json

from .models import Conversation, Message

class ChatConsumer(WebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.conversation: Conversation | None = None
        self.conversation_id: str | None = None

    def connect(self):
        self.conversation_id = self.scope["url_route"]["kwargs"]["conversation_id"]
        try:
            self.conversation = Conversation.objects.get(id=self.conversation_id)
            self.accept()
        except Conversation.DoesNotExist:
            self.close()
            return
        else:
            async_to_sync(self.channel_layer.group_add)( # type: ignore
                self.conversation_id,
                self.channel_name
            )

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)( # type: ignore
            self.conversation_id,
            self.channel_name
        )
    
    def receive(self, text_data=None, bytes_data=None):
        if text_data:
            text_data_json = json.loads(text_data)
            message = text_data_json["message"]

            async_to_sync(self.channel_layer.group_send)( # type: ignore
                self.conversation_id,
                {
                    "type": "chat_message",
                    "message": message,
                }
            )

    def chat_message(self, event):
        message = event["message"]

        self.send(text_data=json.dumps({
            "message": message
        }))
    
