#!/usr/bin/python3
''' user class that inherit from BaseModel'''
class user(BaseModel):
    def __init__(self, email="", password ="", first_name ="", last_name=""):
        '''Constructor'''
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
