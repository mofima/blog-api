from rest_framework import serializers

from drf_spectacular.utils import extend_schema_field

from .models import Category, Article, Comment


class CommentSerializer(serializers.ModelSerializer):
    article_name: str = serializers.SerializerMethodField()
    author_name: str = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            "id",
            "text",
            "article",
            "article_name",
            "author_name",
            "author",
            "created_at",
        ]

    @extend_schema_field(str)
    def get_article_name(self, obj) -> str:
        return obj.article.topic

    @extend_schema_field(str)
    def get_author_name(self, obj) -> str:
        return obj.author.username


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "name",
        ]


class ArticleSerializer(serializers.ModelSerializer):
    category_name: str = serializers.SerializerMethodField()
    author_name: str = serializers.SerializerMethodField()

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

    @extend_schema_field(str)
    def get_category_name(self, obj) -> str:
        return obj.category.name

    @extend_schema_field(str)
    def get_author_name(self, obj) -> str:
        return obj.author.username
