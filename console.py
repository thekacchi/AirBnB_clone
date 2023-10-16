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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
