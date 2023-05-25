#!/usr/bin/python3
"""
Unittests for 'models/base_model.py'
"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModelInstantiation(unittest.TestCase):
    """
    Test cases to ensure correct instantiation of the 'BaseModel' class.
    """

    def test_instantiation_without_args(self):
        """
        Test instantiation of BaseModel without any arguments.
        """
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        """
        Test if a new BaseModel instance is stored in storage.
        """
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        """
        Test the type of the id attribute of BaseModel.
        """
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        """
        Test the type of the created_at attribute of BaseModel.
        """
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        """
        Test the type of the updated_at attribute of BaseModel.
        """
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        """
        Test that two BaseModel instances have unique IDs.
        """
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_models_different_created_at(self):
        """
        Test that two BaseModel instances have different created_at timestamps.
        """
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_two_models_different_updated_at(self):
        """
        Test that two BaseModel instances have different updated_at timestamps.
        """
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.updated_at, bm2.updated_at)

    def test_str_representation(self):
        """
        Test the string representation of a BaseModel instance.
        """
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)

    def test_args_unused(self):
        """
        Test instantiation of BaseModel with unused arguments.
        """
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """
        Test instantiation of BaseModel with keyword arguments.
        """
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """
        Test instantiation of BaseModel with None keyword arguments.
        """
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        """
        Test instantiation of BaseModel with both args and kwargs.
        """
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)


if __name__ == "__main__":
    unittest.main()
