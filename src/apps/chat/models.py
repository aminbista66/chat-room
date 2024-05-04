from django.db import models
from src.apps.auth.models import User, Tag
import uuid




class Conversation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=True, blank=True)
    participants = models.ManyToManyField(User, related_name="conversations")
    conversation_admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="admin_conversations")
    last_conversation_id = models.UUIDField(null=True, blank=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="conversations", null=True, blank=True)

    blocked_participants = models.ManyToManyField(User, related_name="blocked_conversations")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def join(self, user):
        self.participants.add(user)
        self.save()
    
    def leave(self, user):
        self.participants.remove(user)
        self.save()

    def __str__(self) -> str:
        return f"{self.id}"
    
class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    content = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Message {self.id}"