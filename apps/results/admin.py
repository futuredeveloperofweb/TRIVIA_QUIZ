from django.contrib import admin
from .models import Result


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('result_id', 'quiz_id', 'user_id', 'score', 'created_at')
    search_fields = ('quiz_id__title', 'user_id__username')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
