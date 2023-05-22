#!/usr/bin/python3
"""
in this file we are creating a console that will be
working as the UI in case we haven't developed a front-end
yet
"""

import cmd


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
