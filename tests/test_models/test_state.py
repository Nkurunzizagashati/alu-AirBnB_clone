import unittest
from models.state import State


class TestState(unittest.TestCase):

    def setUp(self):
        # Create a sample State instance for testing
        self.state = State()

    def test_attribute(self):
        # Test if the attribute is initialized correctly
        self.assertEqual(self.state.name, '')

    def test_attribute_type(self):
        # Test if the attribute type is correct
        self.assertIsInstance(self.state.name, str)


if __name__ == '__main__':
    unittest.main()
