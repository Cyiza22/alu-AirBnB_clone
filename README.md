#AirBnB Project
=======================================================================================================
##Project Description
Welcome to the Airbnb project, your first step towards building a full-fledged web application - the Airbnb clone. This initial phase is crucial as it sets the foundation for subsequent projects involving HTML/CSS templating, database storage, API integration, and front-end development. The backend of this project is powered by Python, leveraging its object-oriented programming (OOP) capabilities.

##Description of the console/command interpreter
The command interpreter/console serves as the interface of the application, resembling the Bash shell with a limited set of commands specifically designed for the Airbnb website. Developed with Python OOP programming, it allows users to interact with the backend effectively. Some available commands include:

* show
* create
* update
* destroy
* count

These commands enable users to manage objects within the project, such as creating new users or places, retrieving objects from files or databases, performing operations on objects, updating attributes, and destroying objects.

##How to Start It
To start the console, follow these steps:

1. Clone the repository:
> git clone https://github.com/Cyiza22/alu-AirBnB_clone.git
After cloning the repository you will have a folder called AirBnB_clone. In here there will be several files that allow the program to work.
> /console.py : The main executable of the project, the command interpreter.

> models/engine/file_storage.py: Class that serializes instances to a JSON file and deserializes JSON file to instances

> models/__ init __.py: A unique FileStorage instance for the application

> models/base_model.py: Class that defines all common attributes/methods for other classes.

> models/user.py: User class that inherits from BaseModel

> models/state.py: State class that inherits from BaseModel

> models/city.py: City class that inherits from BaseModel

> models/amenity.py: Amenity class that inherits from BaseModel

> models/place.py: Place class that inherits from BaseModel

> models/review.py: Review class that inherits from BaseModel

2. Navigate to the project repository:
> cd alu-AirBnB_clone

3. Run the command interpreter:
> python console.py

##How to Use It

It can work in two different modes:
**Interactive and Non-interactive.**
###Interactive Mode
In interactive mode, the console will display a prompt (hbnb) indicating that the user can write and execute a command. After the command is run, the prompt will appear again a wait for a new command. This can go indefinitely as long as the user does not exit the program.
> $ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

###Non-Interactive Mode
In non-interactive mode, the shell will need to be run with a command input piped into its execution so that the command is run as soon as the Shell starts. In this mode no prompt will appear, and no further input will be expected from the user.
> $ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

##Available Commands and what they do
| Command | Description |
| quit or EOF | Exits the program |
| Usage | By itself |
| ------- | ------- |
| help | Provides a text describing how to use a command |
| Usage | By itself --or-- help <command> |
| ------- | ------- |
| create | Creates a new instance of a valid `Class`, saves it (to the JSON file) and prints the `id`. Valid classes are: BaseModel, User, State, City, Amenity, Place, Review. |
| Usage | create <classname> |
| ------- | ------- |
| show | Prints the string representation of an instance based on the class name and `id` |
| Usage | show <class name> <id> --or-- <class name>.show(<id>) |
| ------- | ------- |
| destroy | Deletes an instance based on the class name and `id` (saves the change into a JSON file). |

| Usage | destroy <class name> <id> --or-- .destroy() |
| ------- | ------- |
| all | Prints all string representation of all instances based or not on the class name. |
| Usage | By itself or all <class name> --or-- <class name>.all() |
| ------- | ------- |
| update | Updates an instance based on the class name and `id` by adding or updating attribute (saves the changes into a JSON file). |
| Usage | update <class name> <id> <attribute name> "<attribute value>" ---or--- <class name>.update(<id>, <attribute name>, <attribute value>) --or-- <class name>.update(<id>, <dictionary representation>) |
| ------ | ------- |
| count | Retrieve the number of instances of a class. |
| Usage | <class name>.count() |
