#!/usr/bin/python3
from models.base_model import BaseModel
'''State classes'''
class State(BaseModel):
    '''State public class attribute'''
    name =""
    def __init__(self, *args, **kwargs):
        '''initialization'''
        super().__init__(*args, **kwargs)
