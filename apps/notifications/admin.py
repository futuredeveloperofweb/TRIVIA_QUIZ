from django.contrib import admin

from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("notification_id", "user_id", "type", "message", "created_at")
    search_fields = ("user_id__username", "type", "message")
    list_filter = ("type", "created_at")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)
