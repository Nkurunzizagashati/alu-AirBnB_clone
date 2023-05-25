#!/usr/bin/python3

"""
This file contain a class User which will help us to
create users accounts
"""

import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        """Set up any necessary resources before running each test case."""
        self.user = User()

    def tearDown(self):
        """Clean up any resources that were used for testing."""
        pass

    def test_default_attribute_values(self):
        """Test that the default attribute values are set correctly."""
        self.assertEqual(self.user.email, '')
        self.assertEqual(self.user.password, '')
        self.assertEqual(self.user.first_name, '')
        self.assertEqual(self.user.last_name, '')

    def test_setting_attributes(self):
        """Test setting attribute values of a User instance."""
        self.user.email = 'test@example.com'
        self.user.password = 'password123'
        self.user.first_name = 'John'
        self.user.last_name = 'Doe'
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.password, 'password123')
        self.assertEqual(self.user.first_name, 'John')
        self.assertEqual(self.user.last_name, 'Doe')

    def test_inheritance(self):
        """Test that User inherits from BaseModel."""
        self.assertTrue(issubclass(User, BaseModel))

    def test_public_class_attributes(self):
        """Test that the public class attributes of User are present."""
        self.assertTrue(hasattr(User, 'email'))
        self.assertTrue(hasattr(User, 'password'))
        self.assertTrue(hasattr(User, 'first_name'))
        self.assertTrue(hasattr(User, 'last_name'))

    def test_instance_is_base_model_instance(self):
        """Test that a User instance is also an instance of BaseModel."""
        self.assertIsInstance(self.user, BaseModel)

    def test_attribute_types(self):
        """Test that attribute types are correct."""
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)


if __name__ == '__main__':
    unittest.main()
