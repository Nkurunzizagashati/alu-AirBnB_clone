#!/usr/bin/python3

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def test_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, '')

    def test_name_setter(self):
        amenity = Amenity()
        amenity.name = 'Wifi'
        self.assertEqual(amenity.name, 'Wifi')

    def test_to_dict(self):
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict['name'], '')

    def test_from_dict(self):
        amenity_dict = {'name': 'Wifi'}
        amenity = Amenity(**amenity_dict)
        self.assertEqual(amenity.name, 'Wifi')

    def test_str_representation(self):
        amenity = Amenity()
        str_representation = str(amenity)
        self.assertIn("'name': ''", str_representation)

    def test_instance_creation_with_id(self):
        amenity_dict = {'id': '123', 'name': 'Wifi'}
        amenity = Amenity(**amenity_dict)
        self.assertEqual(amenity.id, '123')
        self.assertEqual(amenity.name, 'Wifi')


if __name__ == '__main__':
    unittest.main()
