from django.contrib import admin
from .models import Message, Tag, Conversation

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["id", "conversation", "sender", "content", "created_at", "updated_at"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ["id", "last_conversation_id", "created_at", "updated_at"]