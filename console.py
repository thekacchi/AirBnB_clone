#!/usr/bin/python3
""""AirBnB console"""

import cmd

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()

