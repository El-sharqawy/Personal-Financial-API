from django.test import TestCase

from django.contrib.auth import get_user_model

class CustomUserModelTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="testuser@example.com",
            username="testuser",
            password="password123",
            current_balance=100.50
        )

    def test_user_creation(self):
        """Test if a user is created successfully"""
        self.assertEqual(self.user.email, "testuser@example.com")
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.current_balance, 100.50)
        self.assertTrue(self.user.check_password("password123"))

    def test_user_string_representation(self):
        """Test the string representation of the user"""
        self.assertEqual(str(self.user), self.user.username)

    def test_email_uniqueness(self):
        """Test that email field is unique"""
        with self.assertRaises(Exception):
            get_user_model().objects.create_user(
                email="testuser@example.com",
                username="duplicateuser",
                password="password456"
            )

    def test_required_fields(self):
        """Test that email and username are required"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email="testuser2@example.com",
                username="",
                password="password123"
            )

