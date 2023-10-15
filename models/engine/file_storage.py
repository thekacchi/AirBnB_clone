#!/usr/bin/python3
"""
Serialization and deserialization of the JSON file
"""

import json
# from models.base_model import BaseModel


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
            
