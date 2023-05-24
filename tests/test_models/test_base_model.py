import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)
        self.assertIsInstance(b1.id, str)
        self.assertIsInstance(b1.created_at, datetime.datetime)
        self.assertIsInstance(b1.updated_at, datetime.datetime)

        b2 = BaseModel(id="123", created_at="2022-05-24T12:00:00.000000",
                       updated_at="2022-05-24T12:00:00.000000")
        self.assertIsInstance(b2, BaseModel)
        self.assertEqual(b2.id, "123")
        self.assertEqual(b2.created_at,
                         datetime.datetime(2022, 5, 24, 12, 0))
        self.assertEqual(b2.updated_at,
                         datetime.datetime(2022, 5, 24, 12, 0))

    def test_save(self):
        b1 = BaseModel()
        old_updated_at = b1.updated_at
        b1.save()
        self.assertNotEqual(old_updated_at, b1.updated_at)

    def test_to_dict(self):
        b1 = BaseModel()
        b1_dict = b1.to_dict()
        self.assertIsInstance(b1_dict, dict)
        self.assertEqual(b1_dict['__class__'], 'BaseModel')
        self.assertIsInstance(b1_dict['id'], str)
        self.assertIsInstance(b1_dict['created_at'], str)
        self.assertIsInstance(b1_dict['updated_at'], str)
