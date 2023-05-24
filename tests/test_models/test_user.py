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
    self.assertEqual(user.email, "example@example.com")
    self.assertEqual(user.password, "password123")
    self.assertEqual(user.first_name, "John")
    self.assertEqual(user.last_name, "Doe")
