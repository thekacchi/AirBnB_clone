#!/usr/bin/python3
import cmd

"""AirBnB console """

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        print()
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

