"""Import the cmd module"""
import cmd

"""define a subclass of cmd.Cmd"""
class HBNBCommand(cmd.Cmd):
    """define the custom prompt"""
    prompt = "(hbnb) "

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
        """create an instance of HBNB command and start the loop"""
        HBNBCommand().cmdloop()
