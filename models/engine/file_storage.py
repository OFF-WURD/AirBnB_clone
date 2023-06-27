#!/bin/bash/python3
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.city import City
classes = {"BaseModel":BaseModel, "User":User, "State":State, 
           "Place":Place, "Review":Review, "Amenity":Amenity, "City":City}
class FileStorage:
    '''serializes instances to a JSON file and
      deserializes JSON file to instances'''
    #class private Attribute
class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""

    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

def all(self, class_name=None):
    """Returns a dictionary of all objects or objects of a specific class"""
    if class_name:
        objects = {key: obj for key, obj in self.__objects.items()
                   if obj.__class__.__name__ == class_name}
    else:
        objects = self.__objects.copy()
    return objects


    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except:
            pass
