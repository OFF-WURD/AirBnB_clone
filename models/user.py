#!/usr/bin/python3
from models.base_model import BaseModel
''' user class that inherit from BaseModel'''
class user(BaseModel):
    '''user public attribute'''
    email =""
    password =""
    first_name =""
    last_name =""

    def __init__(self, *args, **kwargs):
        '''initialize user'''
        super().__init__(*args, **kwargs)
