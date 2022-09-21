from django.contrib import admin
from .models import Announce, Comment


@admin.register(Announce)
class AnnounceAdmin(admin.ModelAdmin):
    list_display = ("author", "date", "hour", "location", "desired_level")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "email", "announce", "published_date", 'is_active')
    list_filter = ("is_active", "published_date", "updated_date")
    search_fields = ('author', "email", "body")
