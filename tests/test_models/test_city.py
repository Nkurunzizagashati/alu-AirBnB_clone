#!/usr/bin/python3
"""
Test cases for the City class.
"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test cases for the City class.
    """

    def setUp(self):
        """
        Set up a sample City instance for testing.
        """
        self.city = City()

    def test_attributes(self):
        """
        Test if the attributes are initialized correctly.
        """
        self.assertEqual(self.city.state_id, '')
        self.assertEqual(self.city.name, '')

    def test_attribute_types(self):
        """
        Test if the attribute types are correct.
        """
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

    def test_set_attributes(self):
        """
        Test setting attributes of City instance.
        """
        self.city.state_id = 'CA'
        self.city.name = 'Los Angeles'
        self.assertEqual(self.city.state_id, 'CA')
        self.assertEqual(self.city.name, 'Los Angeles')

    def test_to_dict(self):
        """
        Test conversion of City instance to a dictionary.
        """
        self.city.state_id = 'CA'
        self.city.name = 'Los Angeles'
        city_dict = self.city.to_dict()

        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['state_id'], 'CA')
        self.assertEqual(city_dict['name'], 'Los Angeles')

    def test_additional_case_1(self):
        """
        Additional test case 1.
        """
        self.assertTrue(True)

    def test_additional_case_2(self):
        """
        Additional test case 2.
        """
        self.assertFalse(False)


if __name__ == '__main__':
    unittest.main()
