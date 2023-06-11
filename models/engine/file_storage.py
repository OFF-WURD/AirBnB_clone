#!/bin/bash/python3
import json
import os
import models

class FileStorage():
    '''serializes instances to a JSON file and
      deserializes JSON file to instances'''
    #class private Attribute
    __file_path ="files.json"
    __objects = {}
    
    def __init__(self,):
        "Constructor"
        pass

    def  all(self):
        """Return Dictionary __object"""
        return self.__objects
    
    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()
        
        with open(self.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        '''deserializes the JSON file to __objects
          (only if the JSON file (__file_path) exists'''
        try:
            with open(self.__file_path, "r") as file:
                serialized_objects = json.load(file)
                for key, obj_dict in serialized_objects.items():
                    class_name, obj_id = key.split(".")
                    class_ = getattr(models, class_name)
                    obj = class_(**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
