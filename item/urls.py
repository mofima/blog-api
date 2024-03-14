from django.urls import path

from . import views


app_name = "item"
urlpatterns = [
    path("article/", views.ArticleListCreate.as_view(), name="article_list_create"),
    path("article/browse/", views.BrowseApiView.as_view(), name="browse"),
    path("article/<uuid:pk>/", views.ArticleDetail.as_view(), name="article_detail"),
    path(
        "article/<uuid:pk>/comment/",
        views.CommentCreateAPIView.as_view(),
        name="comment_create",
    ),
    path("article/comments/", views.CommentListAPIView.as_view(), name="comment_list"),
    path("article/categories/", views.CategoryList.as_view(), name="category_list"),
]
