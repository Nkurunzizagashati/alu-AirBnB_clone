from models.engine.file_storage import FileStorage
"""
    we are importing FileStorage class to use it in
    this file
"""

__all__ = ["BaseModel", "User", "FileStorage",
           "Amenity", "State", "City", "Place", "Review"]


storage = FileStorage()
storage.reload()
