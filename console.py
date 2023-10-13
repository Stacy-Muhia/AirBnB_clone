#!/usr/bin/python3
"""
This is a program that contains entry points of the command line intepreter
"""


import cmd
import json
from models.base_model import BaseModel
import shlex


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        args = shlex.split(line)
        if not args:
            print("** class name missing **")    
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
    
    def emptyline(self):
        pass


    def do_show(self, line):
        """ Prints the string representation of an instance based on the class name"""

        args = shlex.split(line)
        if not args:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_id = args[1]
            all_objs = BaseModel.all()
            key = "{}.{}".format("BaseModel", obj_id)
            if key in all_objs:
                print(all_objs[key])
            else:
                 print("** no instance found **")

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Also exits the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
