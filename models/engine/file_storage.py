#!/usr/bin/python3
"""
file_storage Module
"""

import json
import os
from models.base_model import BaseModel

class FileStorage:
    """Class for serializing and deserializing objects to/from JSON file."""

    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """Add a new object to the storage dictionary."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def all(self):
        """
        returns the storage dictionary.
        """
        return FileStorage.__objects

    def save(self):
        """
        serializes __objects to the JSON file.
        """
        objects = FileStorage.__objects
        object_dict = {}
        for obj in objects.keys():
            object_dict[obj] = objects[obj].to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(object_dict, f)

    def reload(self):
        """
        Deserialize JSON file to __objects if it exists.
        do nothing if it doesn't.
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                try:
                    object_dict = json.load(f)
                    for key, value in object_dict.items():
                        class_name, object_id = key.split('.')
                        class_cls = eval(class_name)
                        instance_cls = class_cls(**value)
                        FileStorage.__objects[key] = instance_cls
                except Exception:
                    pass
