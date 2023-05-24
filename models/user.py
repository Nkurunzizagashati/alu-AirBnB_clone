#!/usr/bin/python3

"""
This file contain a class User which will help us to
create users accounts
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
        this class will help us to create users
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
