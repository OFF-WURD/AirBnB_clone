#!/usr/bin/python3
from models.base import BaseModel
'''State classes'''
class State(BaseModel):
    '''State public class attribute'''
    name =""
    def __init__(self, *args, **kwargs):
        '''initialization'''
        super().__init__(*args, **kwargs)
