from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class UserType(models.TextChoices):
    CRM = "CRM", "CRM"
    PORTAL = "PORTAL", "PORTAL"

class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_type = models.CharField(max_length=10, choices=UserType.choices, default=UserType.CRM)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="users", null=True, blank=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="users", null=True, blank=True)
    
    def __str__(self) -> str:
        return self.username