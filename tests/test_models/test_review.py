#!/usr/bin/python3
"""
defining class Reviews which will help us to show the reviews of
places
"""

import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):

    def setUp(self):
        """
        Set up any necessary resources before running each test case.
        """
        self.review = Review()

    def tearDown(self):
        """
        Clean up any resources that were used for testing.
        """
        pass

    def test_default_attribute_values(self):
        """
        Test that the default attribute values are set correctly.
        """
        self.assertEqual(self.review.place_id, '')
        self.assertEqual(self.review.user_id, '')
        self.assertEqual(self.review.text, '')

    def test_setting_attributes(self):
        """
        Test setting attribute values of a Review instance.
        """
        self.review.place_id = 'place1'
        self.review.user_id = 'user1'
        self.review.text = 'This is a review'
        self.assertEqual(self.review.place_id, 'place1')
        self.assertEqual(self.review.user_id, 'user1')
        self.assertEqual(self.review.text, 'This is a review')

    def test_inheritance(self):
        """
        Test that Review inherits from BaseModel.
        """
        self.assertTrue(issubclass(Review, BaseModel))

    def test_public_class_attributes(self):
        """
        Test that the public class attributes of Review are present.
        """
        self.assertTrue(hasattr(Review, 'place_id'))
        self.assertTrue(hasattr(Review, 'user_id'))
        self.assertTrue(hasattr(Review, 'text'))

    def test_instance_is_base_model_instance(self):
        """
        Test that a Review instance is also an instance of BaseModel.
        """
        self.assertIsInstance(self.review, BaseModel)

    def test_attribute_types(self):
        """
        Test that attribute types are correct.
        """
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)


if __name__ == '__main__':
    unittest.main()
