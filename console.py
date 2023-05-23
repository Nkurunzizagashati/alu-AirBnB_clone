#!/usr/bin/python3
"""
in this file we are creating a console that will be
working as the UI in case we haven't developed a front-end
yet
"""

import cmd
import models
import shlex
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
        this is HBNBCommand which inherit cmd.Cmd
    """
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """this method will exit the terminal"""
        return True
    
    def do_EOF(self, arg):
        """this method will also exit the terminal"""
        print()
        return True
    
    def emptyline(self):
        """If a user types an empty line the console must pass"""
        pass

    def do_create(self, arg):
        """
        this method will create an instance of BaseModel

        usage: create <class name>
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        class_name = args[0]
        try:
            instance = eval(class_name)()
            instance.save()
            print(instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        this method will prints the string representation
        of an instance based on the class name 
        
        usage: show <class name> <id>
        """
        line = line.split()
        if not line:
            print("** class name missing **")
        elif line[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(line) == 1:
            print("** instance id missing **")
        else:
            class_id = line[1]
            class_name = line[0]
            objects = models.storage.all()
            key = class_name + "." + class_id
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file). 

        usage: destroy <BaseModel> <1234-1234-1234>.
        """
        line = line.split()
        if not line:
            print("** class name missing **")
        elif line[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(line) < 2:
            print("** instance id missing **")
        else:
            class_name = line[0]
            class_id = line[1]
            objects = models.storage.all()
            key = class_name + "." + class_id
            if key in objects:
                del objects[key]
            else:
                print("** no instance found **")


    def do_all(self, line=None):
        """
        Prints all string representation of 
        all instances based or not on the class name. 
        usage: all <BaseModel> or  all
        """
        line = line.split()
        if not line:
            for value in models.storage.all().values():
                print(str(value))
        elif line[0] not in models.classes:
            print("** class doesn't exist **")
        else:
            class_name = line[0]
            for key in models.storage.all().keys():
                if key.split('.')[0] == class_name:
                    print(str(models.storage.all()[key]))

    def do_update(self, line):
        """
        Updates an instance based on the class name and 
        id by adding or updating attribute (save the change into the JSON file)

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        line = line.split()
        if not line:
            print("** class name missing **")
        elif line[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(line) < 2:
            print("** instance id missing **")
        elif len(line) < 3:
            print("** attribute name missing **")
        elif len(line) < 4:
            print("** value missing **")
        elif not (line[0] + "." + line[1]) in models.storage.all().keys():
            print("** no instance found **")
        else:
            key = line[0] + "." + line[1]
            attribute_name = line[2]
            new_value_of_attribute = line[3]
            if line[2] == "created_at" or line[2] == "updated_at" or line[2] == "id":
                print(f"you are not allowed to edit the {line[2]} property")
            else:
                setattr(models.storage.all()[key], attribute_name, new_value_of_attribute)
                models.storage.save()
    
if __name__ == "__main__":
    HBNBCommand().cmdloop()
