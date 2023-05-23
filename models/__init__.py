from models.engine.file_storage import FileStorage
"""
    we are importing FileStorage class to use it in
    this file
"""

__all__ = ["BaseModel", "User"]


storage = FileStorage()
storage.reload()