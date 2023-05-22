#!/usr/bin/python3

import cmd
"""
    we imported cmd module, this module is the one which
    cna help us to create our own console(shell)
"""


class HBNBCommand(cmd.Cmd):
    """
        this is HBNBCommand which inherit cmd.Cmd
    """
    prompt = "(hbnb)"

    def do_quit():
        """this method will exit the terminal"""
        return True
    
    def do_EOF():
        """this method will also exit the terminal"""
        print()
        return True
    
if __name__ == "__main__":
    HBNBCommand().cmdloop()