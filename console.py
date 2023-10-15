#!/usr/bin/python3
""""AirBnB console"""

import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User

valid_class_names = ["BaseModel"]

class HBNBCommand(cmd.Cmd):
     """
    The entry point for the console
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command """
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_create(self, arg):
        """
           Creates a new instance.
           saves it (in JSON file and prints the id
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in valid_class_names:
            print("** class doesn't exist **")
            return

        new_instance = HBNBCommand.valid_class_names[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.valid_class_names:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_objs = storage.all()
        obj = all_objs.get(key)
        if obj:
            print(obj)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.valid_class_names:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_objs = storage.all()
        obj = all_objs.get(key)
        if obj:
            del all_objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        if not arg:
            all_objs = storage.all()
            objs_list = []
            for obj in all_objs.values():
                objs_list.append(str(obj))
            print(objs_list)

    def do_update(self, arg):
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.valid_class_names:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_objs = storage.all()
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
        try:
            attr_type = type(getattr(obj, attribute))
            value = attr_type(value)
        except AttributeError:
            pass
        setattr(obj, attribute, value)
        obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

