#!/usr/bin/env python3
""" Class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances
"""

import json
from os import read
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os.path


class FileStorage:
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        key = obj.__class__.__name__+"." + obj.id
        self.__objects[key] = obj

    def save(self):
        dictionary = {}
        with open(self.__file_path, 'w') as f:
            for obj in self.__objects.values():
                key = obj.__class__.__name__ + "." + obj.id
                dictionary[key] = obj.to.dict()
            json.dump(dictionary, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                my_dict = json.load(f)
                for key, value in my_dict.items():
                    new_object = key.split('.')
                    class_name =  new_object[0]
                    self.new(eval("{}".format(class_name))(**value))
        except FileNotFoundError:
            pass