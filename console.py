#!/usr/bin/python3
""""AirBnB console"""

import cmd

valid_class_names = ["BaseModel", "User", "Place", "Review"]

class HBNBCommand(cmd.Cmd):
    """
    The entry point for the console
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def create(self):
        """
           Creates a new instance.
           saves it (to the JSON file) and prints the id
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in valid_class_names:
            print("** class doesn't exist **")
            return

        new_instance = classes[class_name]()
        new_instance.save()
        print(new_instance.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

