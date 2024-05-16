import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """Class for serializing and deserializing objects to/from JSON file."""

    FILE_PATH = "file.json"

    def __init__(self):
        self.__objects = {}
        self.__count = {'BaseModel': 0, 'User': 0, 'State': 0,
                        'City': 0, 'Amenity': 0, 'Place': 0,
                        'Review': 0}

    def count(self):
        """Return the count of objects."""
        return self.__count

    def all(self):
        """Return all objects."""
        return self.__objects

    def new(self, obj):
        """Add a new object to the storage."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
        self.__count[obj.__class__.__name__] += 1

    def save(self):
        """Serialize objects to JSON file."""
        json_data = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.FILE_PATH, "w") as json_file:
            json.dump(json_data, json_file)

    def reload(self):
        """Deserialize JSON file into objects."""
        class_dict = {
            'BaseModel': BaseModel, 'User': User, 'State': State,
            'City': City, 'Amenity': Amenity, 'Place': Place,
            'Review': Review
        }
        try:
            with open(self.FILE_PATH, "r") as json_file:
                json_data = json.load(json_file)
            for key, data in json_data.items():
                class_name, obj_id = key.split(".")
                if class_name in class_dict:
                    obj = class_dict[class_name](**data)
                    self.__objects[key] = obj
                    self.__count[class_name] += 1
        except FileNotFoundError:
            pass
