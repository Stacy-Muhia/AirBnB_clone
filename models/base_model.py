#!/usr/bin/python3
"""
    This module contains BaseModel class that defines all the
     common attributes/methods for other classes.
     """
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    This BaseModel class defines all common attributes/methods
    for other classes.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialises the instance attributes.
        Args:
            *args
            **kwargs"""
        if len(kwargs) == 0:
            """
            Checks if the **kwargs dict is empty and  generates
            unique ID created_at and updated_at setting them to
            current date and time.
            """
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)

    def __str__(self):
        """
        Returns the informal string representation.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at with
        the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of
        __dict__ of the instance.
        """
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
