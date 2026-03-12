from django.contrib import admin
from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "course",
        "rating",
        "is_approved",
        "created_at"
    )

    list_filter = (
        "rating",
        "is_approved"
    )

    search_fields = (
        "name",
        "content"
    )