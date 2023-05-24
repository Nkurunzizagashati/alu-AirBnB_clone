import unittest
from models.review import Review


class TestReview(unittest.TestCase):

    def setUp(self):
        # Create a sample Review instance for testing
        self.review = Review()

    def test_attributes(self):
        # Test if the attributes are initialized correctly
        self.assertEqual(self.review.place_id, '')
        self.assertEqual(self.review.user_id, '')
        self.assertEqual(self.review.text, '')

    def test_attribute_types(self):
        # Test if the attribute types are correct
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)


if __name__ == '__main__':
    unittest.main()
