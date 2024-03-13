from django.contrib import admin

from .models import Article, Category, Comment


admin.site.register(Category)


class ArtcileAdmin(admin.ModelAdmin):
    list_display = ["topic", "category", "author", "created_at"]
    list_filter = ["created_at", "category"]
    search_fields = ["topic", "content"]


admin.site.register(Article, ArtcileAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ["text", "article", "created_by", "created_at"]
    list_filter = ["article", "created_at"]
    search_fields = ["text"]


admin.site.register(Comment, CommentAdmin)
