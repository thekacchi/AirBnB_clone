#!/usr/bin/python3
"""This module contains the cmd loop and methods"""

import cmd
import models
from models.base_model import BaseModel
from datetime import datetime
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """The HBNBC command Interpreter"""
    prompt = "(hbnb) "
    valid_classes = {"BaseModel", "City", "Place", "State",
                     "Review", "Amenity", "User"}

    def emptyline(self):
        """Empty line (no input)"""
        pass

    def do_create(self, args):
        """
           Creates a new instance of a specified class/model
           and saves it to the JSON file.
           Usage: create <class_name>
        """
        try:
            if not args:
                raise SyntaxError()

            model, *rest = args.split(" ")

            if model in self.valid_classes:
                new_instance = eval(model)()
                models.storage.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")
        except SyntaxError:
            print("** class name missing **")

    def do_show(self, arg):
        """
           Prints the string representation of an instance
           based on the class name and id
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        all_objs = models.storage.all()
        obj = all_objs.get(key)
        if obj:
            print(obj)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
           Deletes an instance based on the class name
           and id (saves the change into the JSON file).
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        all_objs = models.storage.all()
        obj = all_objs.get(key)
        if obj:
            del all_objs[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
           Prints all string representation of all instances
           Based or not on the class name.
        """
        args = arg.split()
        all_objs = models.storage.all()
        objs_list = []
        if not arg:
            for obj in all_objs.values():
                objs_list.append(str(obj))
        else:
            # Class name is provided
            if args[0] not in HBNBCommand.valid_classes:
                print("** class doesn't exist **")
                return
            for key, obj in all_objs.items():
                if key.split('.')[0] == args[0]:
                    objs_list.append(str(obj))
        print(objs_list)

    def do_update(self, arg):
        """The update method"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_objs = models.storage.all()
        obj = all_objs.get(key)
        if not obj:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute = args[2]
        value = args[3]
        if hasattr(obj, attribute):
            if attribute == "created_at" or attribute == "updated_at":
                pass
            else:
                attr_type = type(getattr(obj, attribute))
                try:
                    value = attr_type(value)
                except ValueError as ve:
                    print(f"Error: Invalid value - {ve}")
                setattr(obj, attribute, value)
                obj.save()

    def do_quit(self, arg):
        """Quits the cmd module"""
        return True

    def do_EOF(self, arg):
        """End of file method"""
        print()
        return True

    def count(self, model):
        """Retieves rhe number of instances of a class"""
        if model not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        print(len([y for y in models.storage.all().values()
	           if type(y) is eval(model)]))

    def default(self, cmd_line):
        """Executes customized models commands"""
        callback = {"all": self.do_all,
	            "update": self.do_update,
	            "count": self.count,
		    "destroy": self.do_destroy,
		    "show": self.do_show}
        cmd_list = cmd_line.split('.')

        if len(cmd_list) >= 2:
            command = self.command(cmd_list[1])
            if command not in callback:
                cmd.Cmd.default(self, cmd_line)
                return

            if command in("all", "count"):
                callback[command](cmd_list[0])
            elif command == "update":
                args = self.argtok(cmd_list)
                if isinstance(args, list):
                    key = args[0] + ' ' + args[1]
                    for k, v in args[2].items():
                        self.do_update(key + ' "{}" "{}"'.format(k, v))
                else:
                    self.do_update(args)
            else:
                callback[command](self.argtok(cmd_list))
        else:
            cmd.Cmd.default(self, line)

    def command(self, arg):
        """Command complements default"""
        index = arg.find("(")
        if index == -1:
            return arg
        return arg[:index]

    def argtok(self, args):
        """"Tokenizes args, Cleans too"""

        tokens = []
        tokens.append(args[0])
        try:
            my_dict = eval(
                           args[1][args[1].find('{'):args[1].find('}')+1])
        except Exception:
            my_dict = None
        if isinstance(my_dict, dict):
            new_str = args[1][args[1].find('(')+1:args[1].find(')')]
            tokens.append(((new_str.split(", "))[0]).strip('"'))
            tokens.append(my_dict)
            return tokens
        new_str = args[1][args[1].find('(')+1:args[1].find(')')]
        tokens.append(" ".join(new_str.split(", ")))
        return " ".join(i for i in tokens).strip()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
