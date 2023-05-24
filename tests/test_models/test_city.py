import unittest
from models.city import City


class TestCity(unittest.TestCase):
    city = City()
    city.state_id = '121212'
    city.name = "Kigali"
    city.assertIsInstance(city, City)
    city.assertIsInstance(city.state_id, str)
    city.assertIsInstance(city.name, str)
    city.assertEqual(city.state_id, "121212")
    city.assertEqual(city.name, "Kigali")
