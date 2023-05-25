#!/usr/bin/python3

"""This file contain a class that will help us to create states"""

import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):

    def setUp(self):
        """Set up any necessary resources before running each test case."""
        self.state = State()

    def tearDown(self):
        """Clean up any resources that were used for testing."""
        pass

    def test_default_attribute_values(self):
        """Test that the default attribute values are set correctly."""
        self.assertEqual(self.state.name, '')

    def test_setting_attribute(self):
        """Test setting attribute value of a State instance."""
        self.state.name = 'California'
        self.assertEqual(self.state.name, 'California')

    def test_inheritance(self):
        """Test that State inherits from BaseModel."""
        self.assertTrue(issubclass(State, BaseModel))

    def test_public_class_attributes(self):
        """Test that the public class attributes of State are present."""
        self.assertTrue(hasattr(State, 'name'))

    def test_instance_is_base_model_instance(self):
        """Test that a State instance is also an instance of BaseModel."""
        self.assertIsInstance(self.state, BaseModel)

    def test_attribute_types(self):
        """Test that attribute types are correct."""
        self.assertIsInstance(self.state.name, str)


if __name__ == '__main__':
    unittest.main()
