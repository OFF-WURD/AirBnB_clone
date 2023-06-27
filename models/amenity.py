#!/usr/bin/python3
from models.base_model import BaseModel
'''Amenity class that inherit from BaseModel'''
class Amenity(BaseModel):
    name=""
    def __init__(self,*args, **kwargs):
        '''initialization'''
        super().__init__(*args, **kwargs)
