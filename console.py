#!/usr/bin/python3
"""
content module
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models import storage
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.review import Review
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    acceptableClasses = [
        "BaseModel",
        "User",
        "State",
        "Amenity",
        "Place",
        "Review",
        "City"
    ]
    def verifyArgs(self, args, doupdate=False):
        try:
            className = args[0]
        except Exception:
            print("** class name missing **")
            return False
        if className not in HBNBCommand.acceptableClasses:
            print("** class doesn't exist **")
            return False
        try:
            instanceID = args[1]
        except Exception:
            print("** instance id missing **")
            return False
        key = f"{className}.{instanceID}"
        if key not in storage.all():
            print("** no instance found **")
            return False
        if doupdate:
            try:
                attrName = args[2]
            except Exception:
                print("** attribute name missing **")
                return False
            try:
                attrValue = args[3]
            except Exception:
                print("** value missing **")
                return False
        return True
    def split(self, string):
        list = string.split()
        return list
    def do_quit(self, input):
        quit()
    def do_EOF(self, input):
        print()
        quit()
    def do_create(self, input):
        """creates instance of BaseModel"""
        if input is None:
            print("** class name missing **")
        elif input not in HBNBCommand.acceptableClasses:
            print("** class doesn't exist **")
        instance = eval(input + "()")
        storage.new(instance)
        storage.save()
        print(instance.id)
    def do_show(self, input):
        args = self.split(input)
        if not self.verifyArgs(args):
            return
        className = args[0]
        instanceID = args[1]
        key = f"{className}.{instanceID}"
        print(storage.all()[key])
    def do_destroy(self, input):
        """Deletes an instance"""
        args = self.split(input)
        if not self.verifyArgs(args):
            return
        className = args[0]
        instanceID = args[1]
        key = f"{className}.{instanceID}"
        del storage.all()[key]
        storage.save()
    def do_all(self, input):
        output = []
        if input:
            if input not in HBNBCommand.acceptableClasses:
                print("** class doesn't exist **")
                return
            for object in storage.all():
                if isinstance(storage.all()[object], eval(input)):
                    output.append(str(storage.all()[object]))
            print(output)
        else:
            for object in storage.all():
                output.append(str(storage.all()[object]))
            print(output)
    def do_update(self, input):
        args = self.split(input)
        if not self.verifyArgs(args, doupdate=True):
            return
        className = args[0]
        instanceID = args[1]
        attrName = args[2]
        attrValue = args[3]
        key = f"{className}.{instanceID}"
        if attrValue[0] == '"' and attrValue[-1] == '"':
            attrValue = attrValue[1:-1]
        setattr(storage.all()[key], attrName, attrValue)
        storage.save()
    def emptyline(self):
        pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()