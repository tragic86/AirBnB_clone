#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb)'
    def do_all(self, args):
        """print all string representation of all instances based on
        or not on the clas name"""

    def do_cmd(self, args):
        """type \"help\" followed by a command for more info"""
        pass

    def do_create(self, args):
        """Usage: (hbnb) create BaseModel
        create a new instance of BaseModel, saves it to JSON and prints id"""
        pass

    def do_destroy(self, args):
        """ """
        pass

    def do_EOF(self, args):
        """Type \"EOF\" to exit console via EOF"""
        raise SystemExit

    def help_emptyline(self):
        print("Nothing will happen if you press enter without typing something")

    def help_help(self):
        """documentation for help"""
        print("type \"help\" followed by the command")

    def do_quit(self, args):
        """Typing \"quit\" will exit console\n See also \"help EOF\" """
        raise SystemExit

    def do_show(self, args):
        """"""
        pass

    def do_update(self, args):
        """"""
        pass

if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.cmdloop()
