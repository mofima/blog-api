from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile

import io
from PIL import Image


from item.models import Category, Article, Comment


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="secret",
        )

        cls.category = Category.objects.create(name="Music")

        cls.article = Article.objects.create(
            category=cls.category,
            author=cls.user,
            topic="The off season",
            content="this is best album in years",
        )

        cls.comment = Comment.objects.create(
            article=cls.article, created_by=cls.user, text="this is new"
        )

    def generate_photo_file(self):
        file = io.BytesIO()
        image = Image.new("RGBA", size=(50, 50), color=(155, 0, 0))
        image.save(file, "png")
        file.name = "test.png"
        file.seek(0)
        return file

    def test_category_model(self):
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(self.category.name, "Music")
        self.assertEqual(str(self.category), "Music")

    def test_article_model(self):
        # expected_url = reverse("item:detail", kwargs={"pk": self.article.pk})
        # self.assertEqual(self.article.get_absolute_url(), expected_url)
        self.assertEqual(Article.objects.count(), 1)
        self.assertEqual(self.article.category.name, "Music")
        self.assertEqual(self.article.author.username, "testuser")
        self.assertEqual(self.article.topic, "The off season")
        self.assertEqual(self.article.content, "this is best album in years")
        self.assertEqual(str(self.article), "The off season")

    def test_article_readtime(self):
        article = Article.objects.create(
            category=self.category,
            author=self.user,
            topic="Readtime Test",
            content="A longer piece of content for testing readtime calculation.",
        )
        readtime_result = article.get_readtime()
        self.assertIn("min", readtime_result)

    def test_article_image_upload(self):
        image_file = SimpleUploadedFile(
            name="test_image.png",
            content=self.generate_photo_file().read(),
            content_type="image/png",
        )
        article = Article.objects.create(
            category=self.category,
            author=self.user,
            topic="Image Upload Test",
            content="Testing image upload.",
            image=image_file,
        )
        self.assertTrue(article.image.name.startswith("item_images/"))

    # def test_article_content_validation(self):
    #     with self.assertRaises(ValidationError):
    #         Article.objects.create(
    #             category=self.category,
    #             author=self.user,
    #             topic="Validation Test",
    #             content="Too short.",
    #         )

    def test_comment_model(self):
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(self.comment.article.topic, "The off season")
        self.assertEqual(self.comment.created_by.username, "testuser")
        self.assertEqual(self.comment.text, "this is new")
        self.assertEqual(str(self.comment), "this is new")
