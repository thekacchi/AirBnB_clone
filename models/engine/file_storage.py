#!/usr/bin/python3
"""
Serialization and deserialization of the JSON file
"""

import json
from models.base_model import BaseModel


class FileStorage:
    """
    Serialization and deserialization of the JSON file
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        k = type(obj).__name__ + '.' + obj.id
        FileStorage.__objects[k] = obj

    def save(self):
        """
        Serializing __objects to the JSON file
        """
        with open(FileStorage.__file_path, 'w+') as file:
            dictofileobjs = {}
            for k, value in FileStorage.__objects.items():
                dictofileobjs[k] = value.to_dict()
            json.dump(dictofileobjs, file)

    def reload(self):
        """
        Deserialization from the JSON file
        """
          try:
            with open(FileStorage.__file_path, 'r+') as file:
                dictofileobjs = json.loads(file.read())
                for k, value in dictofileobjs.items():
                    class_name, obj_id = k.split('.')
                    FileStorage.__objects[k] = BaseModel(**value)

        except FileNotFoundError:
            pass

