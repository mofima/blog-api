from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions

from .models import Category, Article, Comment
from .permissions import IsOwnerOrReadOnly
from .serializers import CategorySerializer, ArticleSerializer, CommentSerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ArticleListCreate(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Article.objects.all().order_by("-created_at")[0:6]
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CommentCreateAPIView(generics.CreateAPIView):
    permission_classes = permissions.IsAuthenticated
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        article_pk = self.kwargs.get("pk")
        article = get_object_or_404(Article, pk=article_pk)
        serializer.save(article=article, author=self.request.user)


class CommentListAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class BrowseApiView(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        query = self.request.query_params.get("query", "")
        category_id = self.request.query_params.get("category", 0)
        queryset = Article.objects.all()

        if category_id:
            queryset = queryset.filter(category_id=category_id)

        if query:
            queryset = queryset.filter(
                Q(topic__icontains=query) | Q(content__icontains=query)
            )
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
