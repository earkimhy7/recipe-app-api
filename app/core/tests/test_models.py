from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successfully(self):
        """Test creating new user with email"""
        email = "earkimhy7@gmail.com"
        password = "testing123"
        user = get_user_model.objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
