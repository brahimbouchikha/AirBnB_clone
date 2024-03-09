#!/usr/bin/python3
"""create a class"""


class BaseModel:
    """represent a class"""

    def __init__(self, id, created_at, updated_at):
        """Initialize a class"""
        self.uuid = id
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        return f"[BaseModel] ({self.uuid}) {self.__dict__}"
