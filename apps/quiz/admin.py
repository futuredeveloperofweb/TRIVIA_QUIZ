from django.contrib import admin
from .models import Quiz, Question, Option


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('quiz_id', 'title', 'created_by', 'created_at', 'updated_at')
    search_fields = ('title', 'created_by__username')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_id', 'quiz_id', 'question_text', 'question_type', 'created_at', 'updated_at')
    search_fields = ('question_text', 'quiz_id__title')
    list_filter = ('question_type', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('option_id', 'question_id', 'text', 'is_correct', 'created_at', 'updated_at')
    search_fields = ('text', 'question_id__question_text')
    list_filter = ('is_correct', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
