#!/usr/bin/python3
"""The Review class, which inherits from the BaseModel class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class definition of the Review Class"""
    place_id = ""
    user_id = ""
    text = ""
