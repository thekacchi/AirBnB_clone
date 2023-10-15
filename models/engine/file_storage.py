#!/usr/bin/python3
"""
Serialization and deserialization of the JSON file
"""

import json
from models.base_model import BaseModel
from models.user import User  # Import User class

class FileStorage:
    """FileStorage class for serialization and deserialization."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        self._serialize()

    def reload(self):
        """Deserialize the JSON file to __objects."""
        self._deserialize()

    def _deserialize(self):
        """Deserialize the JSON file to objects."""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    if class_name == 'User':
                        self.__objects[key] = User(**value)
                    elif class_name == 'BaseModel':
                        self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass

    def _serialize(self):
        """Serialize __objects to a JSON file."""
        serialized_objs = {}
        for key, value in self.__objects.items():
            serialized_objs[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(serialized_objs, f)

                    if class_type:
                        self.__objects[key] = class_type(**value)
        except FileNotFoundError:
            pass
                    if class_type:
                        self.__objects[key] = class_type(**value)
        except FileNotFoundError:
            pass
