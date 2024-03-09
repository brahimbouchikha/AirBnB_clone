#!/usr/bin/python3
"""create a class"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """represent a class"""

    def __init__(self):
        """Initialize a class"""
        self.uuid = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """Return the str representation of BaseModel instance."""
        className = self.__class__.__name__
        return f"[{className}] ({self.id}) {self.__dict__}"