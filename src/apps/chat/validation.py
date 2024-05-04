from .models import Conversation
from src.apps.auth.models import User

def validate_user(conversation: Conversation, user: User):
    if not conversation.participants.filter(id=user.id).exists():
        return "User is not a participant in the conversation", False
    
    return None, True