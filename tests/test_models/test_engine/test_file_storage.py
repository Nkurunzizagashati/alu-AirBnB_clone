#!/usr/bin/python3

import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models import storage


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.fs = storage

    def tearDown(self):
        """
        Clean up the test environment.
        """
        try:
            os.remove(self.fs._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_all_returns_dictionary(self):
        """
        Test that the all method returns a dictionary.
        """
        self.assertIsInstance(self.fs.all(), dict)

    def test_new_adds_object_to_all(self):
        """
        Test that the new method adds the object to the __objects dictionary.
        """
        bm = BaseModel()
        self.fs.new(bm)
        self.assertIn(f"BaseModel.{bm.id}", self.fs.all())

    def test_save_writes_to_file(self):
        """
        Test that the save method writes to the file.
        """
        bm = BaseModel()
        self.fs.new(bm)
        self.fs.save()

        with open(self.fs._FileStorage__file_path, 'r') as file:
            data = file.read()
            self.assertIn(f"BaseModel.{bm.id}", data)

    def test_reload_loads_objects_from_file(self):
        """
        Test that the reload method loads objects from the file.
        """
        bm = BaseModel()
        bm.save()

        new_storage = storage
        new_storage.reload()

        self.assertIn(f"BaseModel.{bm.id}", new_storage.all())

    def test_add_underscore(self):
        """
        Test the add_underscore method.
        """
        self.assertEqual(self.fs.add_underscore("BaseModel"), "base_model")
        self.assertEqual(self.fs.add_underscore("Review"), "review")
        self.assertEqual(self.fs.add_underscore("Place"), "place")


if __name__ == '__main__':
    unittest.main()
