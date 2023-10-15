#!/usr/bin/python3
"""
This is a program that contains entry points of the command line intepreter
"""


import cmd
import json
from models.base_model import BaseModel
import shlex
from models import storage


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
        """ Prints the string representation of an instance
        based on the class name"""

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

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
        elif args[0] not in BaseModel.__subclasses__():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_id = args[1]
            obj = storage.get(args[0], obj_id)
            if obj:
                obj.delete()
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representations of instances
        based on the class name"""
        args = shlex.split(line)
        if not args:
            objs = storage.all()
            print([str(obj) for obj in objs.values()])
        elif args[0] not in BaseModel.__subclasses__():
            print("** class doesn't exist **")
        else:
            objs = storage.all(args[0])
            print([str(obj) for obj in objs.values()])

    def do_update(self, line):
        """Updates an instance based on the class name and id
        by adding or updating attribute"""
        args = shlex.split(line)
        if not args:
            print("** class name missing **")
        elif args[0] not in BaseModel.__subclasses__():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_id = args[1]
            obj = storage.get(args[0], obj_id)
            if not obj:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                attr_name = args[2]
                attr_value = args[3]
                if hasattr(obj, attr_name):
                    try:
                        attr_value = eval(attr_value)
                    except (NameError, SyntaxError):
                        pass
                    setattr(obj, attr_name, attr_value)
                    obj.save()

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Also exits the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
