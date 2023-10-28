
# AirBnB CLone - The console
![AirBnB](https://i.imgur.com/Nl8vN2G.jpg)


## Introduction


Team project to build a clone of AirBnB.

In this project, the main objective is to create a console. This means that we will build a command interpreter that  will have the functionality to manage the abstraction between objects and how they are stored.


This console will perform the following tasks:

- Create a new object
- Retrieve an object from file
- Perform operations on objects
- Destroy or delete an object


## Instalation

```bash
git clone https://github.com/NicoNethy/holbertonschool-AirBnB_clone.git
```

change to the `AirBnb` directory and run the command:

```bash
 ./console.py
```


### How used the console

The interactive mode involves real-time communication where the user can give instructions and receive immediate responses. Meanwhile, the non-interactive mode implies that the program runs autonomously, without the need for constant user intervention.

In interactive mode

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

in Non-interactive mode

```bash
$ echo "help" | ./console.py
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
```

### Testing

All the tests can be found in the folder named 'tests'.




