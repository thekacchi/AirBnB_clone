#!/usr/bin/python3
"""Implementation of the class User, which inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Contains User Information as its Attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
