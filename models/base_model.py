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
        print()
        print("id: " + self.id)
        print("Created at " + str(self.created_at))
        print("Updated at " + str(self.updated_at))
        print()
        print(type(self.updated_at))
        print()

    def to_dict(self):
        self.__dict__['updated_at'] = str(self.updated_at.isoformat())
        self.__dict__['created_at'] = str(self.created_at.isoformat())
        self.__dict__['__class__'] = self.__class__.__name__
        return self.__dict__

#       @updated_at.setter
#       def save(self):
#           self.updated_at = datetime.datetime.now()

    def __str__(self):
        """override the string displayed by __str__ method"""
        return("[{}] ({}) {}".format
                (self.__class__.__name__, self.id,
                 self.__dict__))



def test():
    h = Base()
    print(h)
    print()
if __name__ == '__main__':
    test()