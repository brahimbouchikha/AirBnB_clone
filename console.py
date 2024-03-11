#!/usr/bin/python3
""" This module defines the entry point of the command interpreter.
    Typical usage example:


    $ ./console
    (hbnb)

    (hbnb) help
    Documented commands (type help <topic>):
    ========================================
    EOF  create  help  quit

    (hbnb)
    (hbnb) quit
    $
"""
import re
import cmd
import json
from models import storage


class HBNBCommand(cmd.Cmd):
    """define the custom prompt"""

    prompt = "(hbnb) "
    
    def do_help(self, arg):
        """To get help on a command, type help <topic>.
        """
        return super().do_help(arg)

    def do_quit(self, arg):
        """quit command to exit programm"""
        return True

    def do_EOF(self, arg):
        """EOFcommand to exit the program"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn't do anything"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()