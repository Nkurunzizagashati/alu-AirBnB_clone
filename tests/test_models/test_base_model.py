#!/usr/bin/python3
"""
Test cases for BaseModel class.
"""

import unittest
import datetime
import models
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def test_init_with_kwargs(self):
        """
        Test initialization of BaseModel instance with keyword arguments.
        """
        data = {
            'id': 'test_id',
            'created_at': '2022-01-01T00:00:00.000',
            'updated_at': '2022-01-02T00:00:00.000',
            'other_key': 'other_value'
        }
        instance = BaseModel(**data)

        self.assertEqual(instance.id, 'test_id')
        self.assertEqual(instance.created_at,
                         datetime.datetime(2022, 1, 1, 0, 0))
        self.assertEqual(instance.updated_at,
                         datetime.datetime(2022, 1, 2, 0, 0))
        self.assertNotIn('other_key', instance.__dict__)

    def test_init_without_kwargs(self):
        """
        Test initialization of BaseModel instance without keyword arguments.
        """
        instance = BaseModel()

        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)
        self.assertIs(models.storage.new_called, True)

    def test_save(self):
        """
        Test saving the BaseModel instance.
        """
        instance = BaseModel()
        previous_updated_at = instance.updated_at

        instance.save()

        self.assertNotEqual(instance.updated_at, previous_updated_at)
        self.assertIs(models.storage.save_called, True)

    def test_to_dict(self):
        """
        Test conversion of BaseModel instance to a dictionary.
        """
        instance = BaseModel()
        instance_dict = instance.to_dict()

        self.assertIsInstance(instance_dict, dict)
        self.assertEqual(instance_dict['__class__'], 'BaseModel')
        self.assertEqual(instance_dict['id'], instance.id)
        self.assertEqual(instance_dict['created_at'],
                         instance.created_at.isoformat())
        self.assertEqual(instance_dict['updated_at'],
                         instance.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
