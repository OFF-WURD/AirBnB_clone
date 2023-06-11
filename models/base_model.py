#!/usr/bin/python3
from datetime import datetime
import uuid

class BaseModel():
    ''' a Baseclass for all other model'''

    def __init__(self):
        '''constructor'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
    

    def __str__(self):
        ''' [<class name>] (<self.id>) <self.__dict__>'''
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        ''' updates the public instance attribute 
        updated_at with the current datetime '''  
        self.updated_at = datetime.now()

    def to_dict(self):
        '''  returns a dictionary containing all 
        keys/values of __dict__ of the instance'''
        
        obj = self.__dict__.copy() #copying instance of a class
        
        #adding class name to the dictionary
        obj[__class__] = type(self).__name__
        obj[self.created_at] = datetime.now().isoformat()
        obj[self.updated_at] = datetime.now().isoformat()
        return obj
