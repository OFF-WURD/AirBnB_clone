#!/usr/bin/python3
''' console base for command'''
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.city import City
import cmd
import json
class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = '(hbnb) '

    valid_classes = {
        'BaseModel',
        'User',
        'Amenity',
        'State',
        'Place',
        'Review',
        'City'
        }

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return

        if arg not in self.valid_classes:
            print("** class doesn't exist **")
            return

        new_instance = eval(arg)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instances = storage.all()
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key in instances:
            print(instances[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        instance_key = class_name + '.' + instance_id

        instances = storage.all(class_name)
        if instance_key in instances:
            del instances[instance_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        instances = storage.all(class_name)
        print([str(instance) for instance in instances.values()])


    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instances = storage.all()
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in instances:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value = args[3].strip('"')
        instance = instances[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

    def do_count(self, arg):
        """Retrieves the number of instances of a class"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        instances = storage.all(class_name)
        print(len(instances))
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
