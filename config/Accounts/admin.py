from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "first_name", "last_name", "email", "club", "region", "last_login", "is_staff", "is_admin", "is_active")
