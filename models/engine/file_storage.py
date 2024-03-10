#!/usr/bin/python3
"""create a class"""


class FileStorage:
    """represent a class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        k = "{}.{}".format(obj__class__.__name__, obj.id)
        FileStorage.__objects[k] = obj


