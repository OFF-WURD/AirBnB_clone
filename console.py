#!/usr/bin/python3
import cmd
class HBNBCommand(cmd.Cmd):
    '''console.py that contains the entry point of the command interpreter:'''
    prompt = '(hbnb)'

    def do_quit(self, args):
        '''Quit the program'''
        return True #returning True will exit the loop
    
    def do_EOF(self, args):
        '''handle the end-of-file character'''
        print() #print a newline before exiting
        return True
    
    def do_help(self, arg):
        """List available commands with 'help' or detailed help with 'help cmd'."""
        super().do_help(arg)
        
    def emptyline(self):
        '''override emptyline not to do anything'''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
