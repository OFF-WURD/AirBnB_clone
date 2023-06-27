#!/usr/bin/python3
from models.base_model import BaseModel
'''review class that inherit from BaseModel'''
class Review(BaseModel)
    place_id=""
    user_id=""
    text=""
    def __init__(self, *args, **kwargs):
        '''initialization'''
        super().__init__(*args, **kwargs)
