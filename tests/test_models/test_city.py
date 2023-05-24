import unittest
from models.city import City


class TestCity(unittest.TestCase):

    def setUp(self):
        # Create a sample City instance for testing
        self.city = City()

    def test_attributes(self):
        # Test if the attributes are initialized correctly
        self.assertEqual(self.city.state_id, '')
        self.assertEqual(self.city.name, '')

    def test_attribute_types(self):
        # Test if the attribute types are correct
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)


if __name__ == '__main__':
    unittest.main()
