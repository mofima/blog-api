from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@email.com",
            password="secret",
        )

        cls.admin_user = get_user_model().objects.create_superuser(
            username="admin", email="admin@email.com", password="secret"
        )

    def test_create_user(self):
        self.assertEqual(get_user_model().objects.count(), 2)
        self.assertTrue(self.user.check_password("secret"))
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "testuser@email.com")
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_create_superuser(self):
        self.assertEqual(get_user_model().objects.count(), 2)
        self.assertTrue(self.admin_user.check_password("secret"))
        self.assertEqual(self.admin_user.username, "admin")
        self.assertEqual(self.admin_user.email, "admin@email.com")
        self.assertTrue(self.admin_user.is_active)
        self.assertTrue(self.admin_user.is_staff)
        self.assertTrue(self.admin_user.is_superuser)
