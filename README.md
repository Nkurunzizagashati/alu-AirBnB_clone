# HBnB: The Console
![HBNB](/img/hbnb_logo.png)

This project is about creating a clone of AirBnB website
In this project which is The console, we will write the backend for the AirBnB website
and also writing creating the console which will help us to interact with our backend before developing the frontent for our website using html and css together with JavaScript.

# USAGE

To interact with this project, while you are in the parent directory of this file type "./console" to open the console.

To see all commands that this console support or recognize, in the opened terminal you can just type help

# Documented commands (type help <topic>):

(hbnb)help

EOF all create destroy help quit show update

(hbnb)

# EXPLANATION OF COMMANDS

1.  create

    this method will create an instance of BaseModel

            usage: create <class name>

2.  quit

    this command exit the terminal

            usage: quit

3.  show

    this method will prints the string representation
    of an instance based on the class name

        usage: show <class name> <id>

4.  destroy

    Deletes an instance based on the class name
    and id (save the change into the JSON file).

        usage: destroy <BaseModel> <1234-1234-1234>.

5.  all::

    Prints all string representation of
    all instances based or not on the class name.

        usage: all <BaseModel> or  all

6.  update

    Updates an instance based on the class name and
    id by adding or updating attribute (save the change into the JSON file)

        Usage: update <class name> <id> <attribute name> "<attribute value>"
