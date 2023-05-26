#!/usr/bin/python3
"""
defining class Place which will help us to create places
in the city which has rooms which can be booked
"""

import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):

    def setUp(self):
        """
        Set up any necessary resources before running each test case.
        """
        self.place = Place()

    def tearDown(self):
        """
        Clean up any resources that were used for testing.
        """
        pass

    def test_default_attribute_values(self):
        """
        Test that the default attribute values are set correctly.
        """
        self.assertEqual(self.place.city_id, '')
        self.assertEqual(self.place.user_id, '')
        self.assertEqual(self.place.name, '')
        self.assertEqual(self.place.description, '')
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_setting_attributes(self):
        """
        Test setting attribute values of a Place instance.
        """
        self.place.name = 'Test Place'
        self.place.description = 'This is a test place'
        self.place.number_rooms = 3
        self.place.number_bathrooms = 2
        self.place.max_guest = 4
        self.place.price_by_night = 100
        self.place.latitude = 51.5074
        self.place.longitude = -0.1278
        self.place.amenity_ids = ['amenity1', 'amenity2']
        self.assertEqual(self.place.name, 'Test Place')
        self.assertEqual(self.place.description, 'This is a test place')
        self.assertEqual(self.place.number_rooms, 3)
        self.assertEqual(self.place.number_bathrooms, 2)
        self.assertEqual(self.place.max_guest, 4)
        self.assertEqual(self.place.price_by_night, 100)
        self.assertEqual(self.place.latitude, 51.5074)
        self.assertEqual(self.place.longitude, -0.1278)
        self.assertEqual(self.place.amenity_ids, ['amenity1', 'amenity2'])

    def test_inheritance(self):
        """
        Test that Place inherits from BaseModel.
        """
        self.assertTrue(issubclass(Place, BaseModel))

    def test_public_class_attributes(self):
        """
        Test that the public class attributes of Place are present.
        """
        self.assertTrue(hasattr(Place, 'city_id'))
        self.assertTrue(hasattr(Place, 'user_id'))
        self.assertTrue(hasattr(Place, 'name'))
        self.assertTrue(hasattr(Place, 'description'))
        self.assertTrue(hasattr(Place, 'number_rooms'))
        self.assertTrue(hasattr(Place, 'number_bathrooms'))
        self.assertTrue(hasattr(Place, 'max_guest'))
        self.assertTrue(hasattr(Place, 'price_by_night'))
        self.assertTrue(hasattr(Place, 'latitude'))
        self.assertTrue(hasattr(Place, 'longitude'))
        self.assertTrue(hasattr(Place, 'amenity_ids'))

    def test_instance_is_base_model_instance(self):
        """
        Test that a Place instance is also an instance of BaseModel.
        """
        self.assertIsInstance(self.place, BaseModel)

    def test_attribute_types(self):
        """
        Test that attribute types are correct.
        """
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)


if __name__ == '__main__':
    unittest.main()
