#!/usr/bin/python3
"""create a class"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """represent a class"""

    def __init__(self, *args, **kwargs):
          """Initialize a class"""
    if len(kwargs) != 0:
        for key, value in kwargs.items():
            if key == "class":
                continue
            if key == "created_at" or key == "updated_at":
                value = datetime.fromisoformat(value)
            setattr(self, key, value)
        return
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return the str representation of BaseModel instance."""
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()


    def to_dict(self):
        """Return a dictionary of baseModel instance

        Includes the key/value of dict of the instance
        the class name of the object
        created_at and updated_at in iso format.
        """

        d = self.__dict__.copy()
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        d["__class__"] = self.__class__.__name__
        return d
