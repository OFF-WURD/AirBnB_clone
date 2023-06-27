#!/usr/bin/python3
''' console base for command'''
from models.base_model import BaseModel
from models import storage
import cmd
import shlex
import json
class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Exit the program and save the data safely"""
        return True

    
    def do_EOF(self, arg):
        """Exit the program and save the data safely
           when user enter CTRL + D """
        return True

    
    def do_help(self, arg):
        """List available commands with 'help' or detailed help with 'help cmd'."""
        super().do_help(arg)

    
    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    
    def do_create(self, arg):
        '''Creates a new instance of BaseModel
           Structure: create [Class Name]'''
        nominal = shlex.split(arg)
        if len(nominal) == 0:
            print("** class name missing")
            return
        if nominal[0] not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.my_dict[my_data[0]]()
        new_instance.save()
        print(new_instance.id)

    
    def do_show(self, arg):
        '''Print the string representation of an 
           instance based on the class name and id
           structure: show [Class Name] [id]'''
        nominal = shlex.split(arg)
        if len(nominal) == 0:
            print("** class name missing **")
            return
        if nominal[0] not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist **")
            return
        if len(nominal) <= 1:
            print("** instance id missing **")
            return
        storage.reload()
        objs_dict = storage.all()
        key = nominal[0] + "." + nominal[1]
        if key in objs_dict:
            obj_instance = str(objs_dict[key])
            print(obj_instance)
        else:
            print("** no instance found **")

    
    def do_destroy(self, arg):
        '''Deletes an instance based on
           class name and id
           structure: destroy [Class Name] [id]'''
        nominal = shlex.split(arg)
        if len(nominal) == 0:
            print("** class name missing")
            return
        if nominal[0] not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist **")
            return
        if len(nominal) <= 1:
            print("** instance id missing")
            return
        storage.reload()
        objs_dict = storage.all()
        key = nominal[0] + "." + nominal[1]
        if key in objs_dict:
            del objs_dict[key]
            storage.save()
        else:
            print("** no instance found **")   

    
    def do_all(self, arg):
        '''Prints all string representation of all instances
          based or not on the class name
          Structure: all [class Name] or all'''
        storage.reload()
        my_json = []
        objects_dict = storage.all()
        if not arg:
            for key in objects_dict:
                my_json.append(str(objects_dict[key]))
            print(json.dumps(my_json))
            return
        nominal = shlex.split(arg)
        if nominal[0] in HBNBCommand.my_dict.keys():
            for key in objects_dict:
                if token[0] in key:
                    my_json.append(str(objects_dict[key]))
            print(json.dumps(my_json))
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and
        id by adding or updating attribute
        (save the change into the JSON file).
        Structure: update [class name] [id] [arg_name] [arg_value]
        """
        if not arg:
            print("** class name missing **")
            return
        my_data = shlex.split(arg)
        storage.reload()
        objs_dict = storage.all()
        if my_data[0] not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist **")
            return
        if (len(my_data) == 1):
            print("** instance id missing **")
            return
        try:
            key = my_data[0] + "." + my_data[1]
            objs_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        if (len(my_data) == 2):
            print("** attribute name missing **")
            return
        if (len(my_data) == 3):
            print("** value missing **")
            return
        my_instance = objs_dict[key]
        if hasattr(my_instance, my_data[2]):
            data_type = type(getattr(my_instance, my_data[2]))
            setattr(my_instance, my_data[2], data_type(my_data[3]))
        else:
            setattr(my_instance, my_data[2], my_data[3])
        storage.save()
if __name__ == '__main__':
    HBNBCommand().cmdloop()
