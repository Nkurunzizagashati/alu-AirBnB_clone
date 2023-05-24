import unittest
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models import storage


class TestFileStorage(unittest.TestCase):
    def test_new(self):
        # Test creating and adding a new object to __objects dictionary
        u = User()
        storage.new(u)
        key = "User." + u.id
        self.assertIn(key, storage.all())

    def test_all(self):
        # Test returning the __objects dictionary
        all_objs = storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_save(self):
        # Test saving objects to file
        u = User()
        storage.new(u)
        storage.save()
        with open(storage._FileStorage__file_path, 'r') as f:
            file_contents = f.read()
            self.assertIn("User." + u.id, file_contents)

    def test_reload(self):
        # Test reloading objects from file
        u = User()
        storage.new(u)
        storage.save()
        storage.reload()
        key = "User." + u.id
        self.assertIn(key, storage.all())
        self.assertIsInstance(storage.all()[key], User)
