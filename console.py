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
        """
        Create an object of any class.
        Example:
            create <class_name>
        """

        if len(args) == 0:
            print("** class name missing **")
            return
        elif args not in self.classes:
            print("** class doesn't exist **")
            return

        new_instance = self.classes[args]()
        storage.save()
        print(new_instance.id)

    def do_show(self, args):
        """
        Showing the string represent an instance of class.
        Example:
            show <class_name> <id>
        """
        args_list = args.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args_list[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        obj_id = args_list[1]
        key = f"{class_name}.{obj_id}"

        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** Instance id not found **")

    def do_destroy(self, args):
        """
        Delete an instance based on the class name and ID if instance.
        Example:
            destroy <class_name> <id>
        """

        args_list = args.split()
        if len(args_list) == 0:
            print("** Class name missing **")
        elif len(args_list < 2):
            print("instance id missing")
        else:
            class_name = args_list[0]
            obj_id = args_list[1]
            key = f"{class_name}.{obj_id}"
            if key in storage.all():
                del storage.all[key]
                storage.save()
            else:
                print("*** no instance found ***")

    def do_all(self, args):
        """
        Print the string representation of all instances
        or a specific class.

        Example:
            all [class_name]
        """

        args_list = args.split()
        if len(args_list) == 0:
            for key, value in storage.all().items():
                print(str(value))
        elif args_list[0] not in self.classes:
            print("*** class doesn't exist***")
        else:
            for key, value in storage.all().items():
                if key.split('.')[0] == args_list[0]:
                    print(str(value))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
