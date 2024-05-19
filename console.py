#!/usr/bin/python3
""" Console Module """

import cmd
import sys
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Contains the functionality for the HBNB console.
    """

    prompt = '(hbnb) '
    classes = {
        'BaseModel': BaseModel,
    }
    
    def do_quit(self, args):
        """
        Method to exit the HBNB console.
        """
        return True

    def help_quit(self):
        """
        Prints the help documentation for quit.
        """
        print("Quit command to exit the program\n")

    def do_EOF(self, arg):
        """
        Handles EOF to exit program.
        """
        print()
        return True

    def help_EOF(self):
        """
        Prints the help documentation for EOF.
        """
        print("Exits the program without formatting\n")

    def do_create(self, args):
        """Create an object of any class"""
        if not args:
            print("** class name missing **")
            return
        elif args not in self.classes:
            print("** class doesn't exist **")
            return

        new_instance = self.classes[args]()
        storage.save()
        print(new_instance.id)




if __name__ == "__main__":
    HBNBCommand().cmdloop()
