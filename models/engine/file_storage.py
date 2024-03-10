#!/usr/bin/python3
"""create a class"""
import os
import json
from models.base_model import BaseModel


class FileStorage:
    """
    serializes instances to a JSON file,
    desrializes JSON file to instance.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with k <obj class name>.id
        """
        k = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[k] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path).
        """
        with open(FileStorage.__file_path, 'w') as f:
            data = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(data, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        only if the JSON file exists; otherwise, does nothing.
        """

        if not os.path.exists(FileStorage.__file_path):
            return
        
        with open(FileStorage.__file_path, 'r') as f:
            data = json.load(f)
            FileStorage.__objects = {k: BaseModel.to_dict(v) for k, v in data.items()}