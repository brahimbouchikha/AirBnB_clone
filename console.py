import cmd
import sys

from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
  """Contains the functionality for the HBNB console"""

  prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

  classes = {
      'BaseModel': BaseModel, 'User': User, 'Place': Place,
      'State': State, 'City': City, 'Amenity': Amenity,
      'Review': Review
  }

  dot_cmds = ['all', 'count', 'show', 'destroy', 'update']

  types = {
      'number_rooms': int, 'number_bathrooms': int,
      'max_guest': int, 'price_by_night': int,
      'latitude': float, 'longitude': float
  }

  def preloop(self):
      """Prints if isatty is false"""
      if not sys.__stdin__.isatty():
          print('(hbnb)')

  def do_quit(self, args):
      """Method to exit the HBNB console"""
      exit()

  def help_quit(self):
      """Prints the help documentation for quit"""
      print("Exits the program with formatting\n")

  def do_EOF(self, args):
      """Handles EOF to exit program"""
      print()
      exit()

  def emptyline(self):
      """Overrides the emptyline method of CMD"""
      pass

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

  def help_create(self):
      """Help information for the create method"""
      print("Creates an instance of a class")
      print("[Usage]: create <class_name>\n")

  def do_show(self, args):
      """Show an individual object"""
      args_list = args.split()

      if not args:
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
          print("** no instance found **")

  def help_show(self):
      """Help information for the show command"""
      print("Shows an individual instance of a class")
      print("[Usage]: show <class_name> <object_id>\n")

if __name__ == "__main__":
  HBNBCommand().cmdloop()
