#!/usr/bin/python3

"""
defining class City which we will use to create
cities where where there is rooms and apartments to book
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    this class City has public class attributes
    state_id: string - empty string: it will be the State.id
    name: string - empty string
    """
    state_id = ''
    name = ''
