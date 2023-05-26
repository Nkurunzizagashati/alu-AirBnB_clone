#!/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.bm = BaseModel()

    def test_instantiation_without_args(self):
        """
        Test instantiation of BaseModel without any arguments.
        """
        self.assertEqual(BaseModel, type(self.bm))

    def test_new_instance_has_unique_id(self):
        """
        Test that each new instance of BaseModel has a unique ID.
        """
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_new_instance_has_created_at_and_updated_at(self):
        """
        Test that each new instance of BaseModel has created_at and updated_at attributes.
        """
        self.assertIsInstance(self.bm.created_at, datetime)
        self.assertIsInstance(self.bm.updated_at, datetime)

    def test_string_representation(self):
        """
        Test the string representation of a BaseModel instance.
        """
        self.assertIn("[BaseModel] (", str(self.bm))
        self.assertIn(") ", str(self.bm))
        self.assertIn("{", str(self.bm))
        self.assertIn("}", str(self.bm))

    def test_save_updates_updated_at(self):
        """
        Test that the save method updates the updated_at attribute.
        """
        before_save = self.bm.updated_at
        self.bm.save()
        self.assertNotEqual(before_save, self.bm.updated_at)

    def test_to_dict_contains_correct_keys(self):
        """
        Test that the to_dict method returns a dictionary containing the correct keys.
        """
        bm_dict = self.bm.to_dict()
        self.assertIn("id", bm_dict)
        self.assertIn("created_at", bm_dict)
        self.assertIn("updated_at", bm_dict)
        self.assertIn("__class__", bm_dict)

    def test_to_dict_created_at_and_updated_at_are_strings(self):
        """
        Test that the to_dict method returns created_at and updated_at attributes as ISO-formatted strings.
        """
        bm_dict = self.bm.to_dict()
        self.assertIsInstance(bm_dict["created_at"], str)
        self.assertIsInstance(bm_dict["updated_at"], str)


if __name__ == '__main__':
    unittest.main()
