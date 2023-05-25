#!/usr/bin/python3

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def setUp(self):
        # Create a sample Amenity instance for testing
        self.amenity = Amenity()

    def test_attribute(self):
        # Test if the attribute is initialized correctly
        self.assertEqual(self.amenity.name, '')

    def test_attribute_type(self):
        # Test if the attribute type is correct
        self.assertIsInstance(self.amenity.name, str)


if __name__ == '__main__':
    unittest.main()
