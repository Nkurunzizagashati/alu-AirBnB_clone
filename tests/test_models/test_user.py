import unittest
from models.user import User


class TestUser(unittest.TestCase):
    # Test creating a new user with valid data
    user = User()
    user.email = "example@example.com"
    user.password = "password123"
    user.first_name = "John"
    user.last_name = "Doe"
    user.assertIsInstance(user, User)
    user.assertEqual(user.email, "example@example.com")
    user.assertEqual(user.password, "password123")
    user.assertEqual(user.first_name, "John")
    user.assertEqual(user.last_name, "Doe")
