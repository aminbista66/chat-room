from django.contrib import admin
from .models import User, Company

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "email", "user_type", "is_active", "is_staff", "is_superuser", "company", "tag"]


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]