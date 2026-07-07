from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin

from .models import Note


@admin.register(Note)
class NoteAdmin(ModelAdmin):
    change_list_template = "admin/notes/note/change_list.html"
    change_form_template = "admin/notes/note/change_form.html"

    list_display = (
        "title",
        "user",
        "status_badge",
        "created_at",
    )

    list_filter = (
        "status",
        "created_at",
    )

    search_fields = (
        "title",
        "content",
        "user__username",
    )

    list_select_related = (
        "user",
    )

    date_hierarchy = "created_at"

    ordering = (
        "-created_at",
    )

    list_per_page = 10

    readonly_fields = (
        "created_at",
    )

    fieldsets = (
        (
            "Note Information",
            {
                "fields": (
                    "user",
                    "title",
                    "content",
                    "status",
                ),
            },
        ),
        (
            "System Information",
            {
                "fields": (
                    "created_at",
                ),
            },
        ),
    )

    actions = (
        "mark_active",
        "mark_archived",
    )

    def status_badge(self, obj):
        color = "#16a34a" if obj.status == "active" else "#6b7280"

        return format_html(
            '<span style="padding:6px 12px;background:{};color:white;border-radius:999px;font-weight:600;">{}</span>',
            color,
            obj.get_status_display(),
        )

    status_badge.short_description = "Status"

    @admin.action(description="Mark selected notes as Active")
    def mark_active(self, request, queryset):
        queryset.update(status="active")

    @admin.action(description="Mark selected notes as Archived")
    def mark_archived(self, request, queryset):
        queryset.update(status="archived")

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}

        extra_context.update(
            {
                "total_notes": Note.objects.count(),
                "active_notes": Note.objects.filter(status="active").count(),
                "archived_notes": Note.objects.filter(status="archived").count(),
            }
        )

        return super().changelist_view(
            request,
            extra_context=extra_context,
        )