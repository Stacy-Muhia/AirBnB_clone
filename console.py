#!/usr/bin/python3
"""
This is a program that contains entry points of the command line intepreter
"""


import cmd
import json


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, args):
        """Creates a new instance of BaseModel"""


    def do_show(self, args):
        """ Prints the string representation of an instance based on the class name"""


    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Also exits the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
