from django.contrib import admin
from .models import Post,Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title","author","write_at","is_active")
    list_filter = ("is_active","write_at")
    list_editable = ("author","is_active")

    readonly_fields = ("write_at","update_at","word_count")
    autocomplete_fields = ("author","categories")

    date_hierarchy = "write_at"

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("__str__","writer","status","write_at",)
    list_filter = ("status","write_at",)
    list_editable = ("writer","status",)

    readonly_fields = ("write_at",)

    date_hierarchy = "write_at"
