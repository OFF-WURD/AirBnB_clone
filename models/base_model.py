#!/usr/bin/python3
import uuid
from datetime import datetime
import models

class BaseModel:
    '''A Baseclass for all other class'''
    
    def __init__(self, *args, **kwargs):
        '''constructor'''
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in['created_at','updated_at']:
                        #convert string to datetime object
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        '''return [<class name>] (<self.id>) <self.__dict__>'''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''updates the public instance attribute updated_at with the current datetime'''
        self.updated_at = datetime.now()
        model.storage.save(self)

    def to_dict(self):
        '''returns a dictionary containing all keys/values of __dict__ of the instance'''
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
