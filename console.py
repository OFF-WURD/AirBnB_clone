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
    
    def help_quit(self):
        '''Display help for the 'quit' command'''
        print('This command exit the programm')
    
    def help_EOF(self):
        '''Display help for the 'EOF' command'''
        print("This command means end-of-file and it exit the program")
    def emptyline(self):
        '''override emptyline not to do anything'''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
