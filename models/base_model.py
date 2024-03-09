#!/usr/bin/python3
"""create a class"""
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """represent a class"""

    def __init__(self):
        """Initialize a class"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return the str representation of BaseModel instance."""
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()

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
