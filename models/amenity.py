#!/usr/bin/python3
"""
defining class Amenity that will help us to create and add
amenities which are available in different places
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Public class attributes:
    name: string - empty string
    """
    name = ''
