#!/usr/bin/python3
"""defines all common methods of other classes with using parent class"""
import uuid
from datetime import datetime
from . import storage

class BaseModel:
    """A base class for all hbnb models"""

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """
        updates the public instance attribute with the current datetime
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        returns a dict containing all keys of __dict__ of the instance
        """

        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat
        inst_dict["updated_at"] = self.updated_at.isoformat

        return inst_dict

    def __str__(self):

        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
