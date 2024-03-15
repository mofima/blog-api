from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.conf import settings

import uuid
import readtime
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ("name",)

    def __str__(self):
        return self.name


def validate_image_size(image):
    # maximum allowed image size
    max_size = 2 * 1024 * 1024  # 2MB

    if image.size > max_size:
        raise ValidationError("Max image size is 2 MB")


class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    topic = models.CharField(max_length=255)
    image = models.ImageField(
        default="images/default_artpic.jpg",
        upload_to="item_images",
        blank=True,
        null=True,
        validators=[validate_image_size],
    )
    content = models.TextField(
        validators=[
            MinLengthValidator(9, "The content must be more than 9 characters long")
        ],
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comments = models.ManyToManyField(
        settings.AUTH_USER_MODEL, through="Comment", related_name="comments_owned"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_readtime(self):
        result = readtime.of_text(self.content)
        return result.text

    def __str__(self):
        return self.topic

    def get_absolute_url(self):
        return reverse("item:detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    text = models.TextField(
        validators=[MinLengthValidator(2, "Comment must be greater than 2 characters")]
    )
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if len(self.text) < 15:
            return self.text
        return self.text[:11] + "..."
