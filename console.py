#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """The HBNBC command"""
    prompt = "(hbnb) "
    valid_classes = ["BaseModel"]

    def emptyline(self):
        pass

    def do_create(self, arg):
        """
           Creates a new instance of a specified class
           and saves it to the JSON file.
           Usage: create <class_name>
        """
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.strip()
        if class_name not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return

        new_instance = HBNBCommand.valid_classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """the show method"""
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
        all_objs = storage.all()
        obj = all_objs.get(key)
        if obj:
            print(obj)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """The destroy method"""
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
        all_objs = storage.all()
        obj = all_objs.get(key)
        if obj:
            del all_objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """the all method"""
        if not arg:
            all_objs = storage.all()
            objs_list = []
            for obj in all_objs.values():
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

    def do_quit(self, arg):
        """Quits the cmd module"""
        return True

    def do_EOF(self, arg):
        """End of file method"""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
