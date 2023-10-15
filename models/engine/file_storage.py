import json
import os
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Add an object to the current database session."""
        key = f"{obj.__class__.__name__}.{obj.id}"
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
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            for key, value in data.items():
                cls_name, obj_id = key.split('.')
                obj = BaseModel(**value)
                self.new(obj)
            return FileStorage.__objects
        except FileNotFoundError:
            pass
            
