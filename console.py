#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    valid_classes = ["BaseModel"]

    def emptyline(self):
        pass

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
            return
        if arg not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return

        new_instance = HBNBCommand.valid_classes[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
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
        args = arg.split()
        all_objs = storage.all()
        objs_list = []
        if not arg:
            for obj in all_objs.values():
                objs_list.append(str(obj))
        else:
            if args[0] not in HBNBCommand.valid_classes:
                print("** class doesn't exist **")
                return
            for key, obj in all_objs.items():
                if key.split('.')[0] == args[0]:
                    objs_list.append(str(obj))
        print(objs_list)

    def do_update(self, arg):
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
        if hasattr(obj, attribute):
            if attribute == "created_at" or attribute == "updated_at":
                pass
            else:
                attr_type = type(getattr(obj, attribute))
                try:
                    value = attr_type(value)
                except ValueError:
                    pass
                setattr(obj, attribute, value)
                obj.save()
    
    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
