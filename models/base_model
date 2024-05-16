#!/usr/bin/python3

import uuid
from datetime import datetime
from typing import Dict

class BaseModel:
    """A base class for all hbnb models"""

    def __init__(self, *args, **kwargs) -> None:
        """Instantiate a new model."""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            try:
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            except KeyError as e:
                raise ValueError(f"Missing required attribute: {e}")
            except ValueError:
                raise ValueError("Invalid datetime format provided")
            self.__dict__.update(kwargs)

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self) -> None:
        """Save the current state of the object."""
        self.updated_at = datetime.now()
        # Call method to save to storage

    def to_dict(self) -> Dict[str, str]:
        """Convert instance into dict format."""
        return {
            **self.__dict__,
            "__class__": self.__class__.__name__,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

