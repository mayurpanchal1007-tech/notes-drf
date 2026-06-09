from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Note

@admin.register(Note)
class NoteAdmin(ModelAdmin):
    list_display = ("title", "user", "created_at", "updated_at")
    list_filter = ("user",)
    search_fields = ("title", "content")
    readonly_fields = ("created_at", "updated_at")