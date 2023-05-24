import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        # Create a sample BaseModel instance for testing
        self.base_model = BaseModel()

    def test_init(self):
        # Test if the attributes are initialized correctly
        self.assertIsNotNone(self.base_model.id)
        self.assertIsNotNone(self.base_model.created_at)
        self.assertIsNotNone(self.base_model.updated_at)
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime.datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime.datetime)

    def test_str(self):
        # Test if the __str__() method returns the correct string representation
        expected_str = f"[BaseModel] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected_str)

    def test_save(self):
        # Test if the save() method updates the updated_at attribute
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict(self):
        # Test if the to_dict() method returns the correct dictionary representation
        dict_rep = self.base_model.to_dict()
        self.assertIsInstance(dict_rep, dict)
        self.assertEqual(dict_rep['__class__'], 'BaseModel')
        self.assertEqual(dict_rep['id'], self.base_model.id)
        self.assertEqual(dict_rep['created_at'],
                         self.base_model.created_at.isoformat())
        self.assertEqual(dict_rep['updated_at'],
                         self.base_model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
