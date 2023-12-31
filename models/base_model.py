#!/usr/bin/python3
"""This is the basee model"""

import models
import uuid
from datetime import datetime


class BaseModel:
    """The BaseModel class definition"""
    def __init__(self, *args, **kwargs):
        """The init method for BaseModel class"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key,
                                datetime.strptime(value,
                                                  "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            """The init method for BaseModel"""
# Generate a unique ID
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """The string method"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """The save method"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """The to_dict mathod"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['id'] = self.id
        obj_dict['created_at'] = self.created_at.isoformat()
        return obj_dict
