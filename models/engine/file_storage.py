#!/usr/bin/python3
"""Implementation of the FileStorage class"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review

class FileStorage:
    """FileStorage class definition"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Add an object to the current database session."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize objects to a JSON file."""
        data = {}
        for key, obj in FileStorage.__objects.items():
            data[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file)

    def reload(self):
        """Deserialize objects from a JSON file."""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            for key, value in data.items():
                class_name, obj_id = key.split('.')
                class_obj = globals()[class_name]
                obj = class_obj(**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
