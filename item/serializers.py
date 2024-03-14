from rest_framework import serializers

from .models import Category, Article, Comment


class CommentSerializer(serializers.ModelSerializer):
    article_name = serializers.SerializerMethodField()
    author_name = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            "id",
            "text",
            "article",
            "article_name",
            "author_name",
            "created_by",
            "created_at",
        ]

    def get_article_name(self, obj):
        return obj.article.topic

    def get_author_name(self, obj):
        return obj.created_by.username


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "name",
        ]


class ArticleSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    author_name = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = [
            "id",
            "category",
            "category_name",
            "author",
            "author_name",
            "topic",
            "content",
            "image",
            "created_at",
            "comments",
        ]

    def get_category_name(self, obj):
        return obj.category.name

    def get_author_name(self, obj):
        return obj.author.username
