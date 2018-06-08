#!/usr/bin/python3
""" Base module for Holberton BnB """
import datetime
import json
import uuid

class BaseModel:
    """initializes the Base method
    Args:
    """

    def __init__(self, id=None):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        print("{}{}{}".format(self.id, self.created_at, self.updated_at))
    def save(self):
        pass

    def to_dict(self):
        pass

    def __str__(self):
        """override the string displayed by __str__ method"""
        return("[{}] ({}) {}".format
                (self.__class__.__name__, self.id,
                 self.__dict__))