# Import the cmd module
import cmd

# Define a subclass of cmd.Cmd
class HBNBCommand(cmd.Cmd):
# Define the custom prompt
prompt = "(hbnb) "

# Define the do_quit method to exit the program
def do_quit(self, arg):
"""Quit command to exit the program"""
return True

# Define the do_EOF method to exit the program
def do_EOF(self, arg):
"""EOF command to exit the program"""
return True

# Define the emptyline method to do nothing
def emptyline(self):
"""An empty line + ENTER shouldn’t execute anything"""
pass

# Check if the file is executed directly
if __name__ == "__main__":
# Create an instance of HBNBCommand and start the loop
HBNBCommand().cmdloop()

