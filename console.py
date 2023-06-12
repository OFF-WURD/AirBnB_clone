#!/usr/bin/python3
"""
This is the console base for the unit
"""
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def do_help(self, arg):
        """List available commands with 'help' or detailed help with 'help cmd'."""
        super().do_help(arg)

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass
    def do_create(self, arg):
        '''Creates a new instance of BaseModel'''
        if not arg:
            print("** class name missing **")
        elif arg not in self.__class__.__name__:
            print("** class doesn't exist **")
        else:
            new_instance = HBNBCommand.eval(arg)()
            new_instance.save()
            print(new_instance.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
