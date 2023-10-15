#!/usr/bin/python3
"""This is the basee model"""

import uuid
from datetime import datetime


class BaseModel:
    """The BaseModel class definition"""
    def __init__(self):
        """The init method for BaseModel"""
# Generate a unique ID
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """The string method"""
        return "[{}] ({}) {}"
        .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """The save method"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """The to_dict mathod"""
        model_dict = self.__dict__.copy()
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()
        return model_dict
