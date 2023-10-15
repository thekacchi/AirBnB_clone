import cmd
import json

class AirBnBCommand(cmd.Cmd):
    """The entry point for the console"""
    prompt = "(airbnb) "

    class_names = ["BaseModel", "User", "Place", "Amenity"]

    def do_create(self, arg):
        """Creates a new instance of a class."""

        args = arg.split()
        class_name = args[0]
        if class_name not in self.class_names:
            print("** class doesn't exist **")
            return

        new_instance = eval(class_name)()  # pylint: disable=eval-used
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Shows an instance of a class."""

        args = arg.split()
        class_name = args[0]
        instance_id = args[1]
        if class_name not in self.class_names:
            print("** class doesn't exist **")
            return

        all_objs = storage.all()
        obj = all_objs.get(f"{class_name}.{instance_id}")
        if obj:
            print(obj)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Destroys an instance of a class."""

        args = arg.split()
        class_name = args[0]
        instance_id = args[1]
        if class_name not in self.class_names:
            print("** class doesn't exist **")
            return

        all_objs = storage.all()
        obj = all_objs.get(f"{class_name}.{instance_id}")
        if obj:
            del all_objs[f"{class_name}.{instance_id}"]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Shows all instances of a class."""

        args = arg.split()
        class_name = args[0]
        if class_name not in self.class_names:
            print("** class doesn't exist **")
            return

        all_objs = storage.all()
        objs_list = []
        for obj in all_objs.values():
            if obj.__class__.__name__ == class_name:
                objs_list.append(str(obj))
        print(objs_list)

    def do_update(self, arg):
        """Updates an instance of a class."""

        args = arg.split()
        class_name = args[0]
        instance_id = args[1]
        attribute_name = args[2]
        new_value = args[3]
        if class_name not in self.class_names:
            print("** class doesn't exist **")
            return

        all_objs = storage.all()
        obj = all_objs.get(f"{class_name}.{instance_id}")
        if obj:
            setattr(obj, attribute_name, new_value)
            obj.save()
        else:
            print("** no instance found **")

    def do_quit(self, arg):
        """Quit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

if __name__ == "__main__":
    AirBnBCommand().cmdloop()
