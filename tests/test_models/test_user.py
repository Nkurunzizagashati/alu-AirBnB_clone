import unittest
from models.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        # Create a sample User instance for testing
        self.user = User()

    def test_attributes(self):
        # Test if the attributes are initialized correctly
        self.assertEqual(self.user.email, '')
        self.assertEqual(self.user.password, '')
        self.assertEqual(self.user.first_name, '')
        self.assertEqual(self.user.last_name, '')

    def test_attribute_types(self):
        # Test if the attribute types are correct
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)


if __name__ == '__main__':
    unittest.main()
