#!/usr/bin/python3
"""
Serialization and deserialization of the JSON file
"""

import json
import os

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.____name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        serialized_objs = {}
        for key, obj in self.__objects.items():
            serialized_objs[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(serialized_objs, f)

    def reload(self):
        """Deserializes the JSON file to __objects if it exists."""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj


class FileStorage:
    """
    Serialization and deserialization of the JSON file
    """
    __file_path = "file.json"
# Path to the json file
    __objects = {}
# Dictionary to store objects

    def all(self):
        """Return the dictionary of objects"""
        return self.__objects

    def new(self, obj):
        """Add new object to the dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializing the saved __objects to the JSON file
        """
        serialized = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized, file)

    def reload(self):
        """
        Deserialize and load objects from the JSON file
        """
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                serialized = json.load(file)
                for key, value in serialized.items():
                    class_name, obj_id = key.split('.')
                    class_type = None
                    for subclass in BaseModel.__subclasses__():
                        if subclass.__name__ == class_name:
                            class_type = subclass
                            break
                    if class_type:
                        self.__objects[key] = class_type(**value)
        except FileNotFoundError:
            pass
            
