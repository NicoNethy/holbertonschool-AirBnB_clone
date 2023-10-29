#!/usr/bin/env python3
""" Clase FileStorage que serializa instancias a un archivo
    JSON y deserializa un archivo JSON a instancias
"""

from os import read
import json
from models.state import State
from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os.path
from models.user import User


class FileStorage:
    """ Clase FileStorage que serializa y
        deserializa instancias a JSON
        __file_path: la ruta del archivo JSON
        __objects: un diccionario de todos los objetos
    """
    def __init__(self):
        """ inicializa FileStorage
        """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Devuelve un diccionario de todos los objetos
        """
        return self.__objects

    def new(self, obj):
        """Coloca en __objects el objeto con la clave <obj class name>.id
        """
        key = obj.__class__.__name__+"." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serealiza __objects en el archivo JSON (path: __file_path)
        dicttionary: un diccionario vacio
        Abre el diccionario en modo de escritura
       Vierte el diccionario en el archivo f
        """
        dictionary = {}
        with open(self.__file_path, 'w') as f:
            for obj in self.__objects.values():
                key = obj.__class__.__name__ + "." + obj.id
                dictionary[key] = obj.to.dict()
            json.dump(dictionary, f)

    def reload(self):
        """Deserealiza el archivo JSON to __objects
        (solo si el archivo JSON (__file_path) existe
        en caso contrario no se hace nada.
        Si el archivo no existe, no deberia generarse ninguna excepción)
        Abrir en modo de lectura"
        Cargar el archivo f y leerlo
        """
        try:
            with open(self.__file_path, 'r') as f:
                my_dict = json.load(f)
                for key, value in my_dict.items():
                    """Este bucle for utiliza un par clave-valor para ejecutar
                    my_dict.items() y crear un diccionario de clave y valor.
                    """
                    new_object = key.split('.')
                    class_name = new_object[0]
                    """new_object es igual a key.split('.')[0]
                    esto divide la clave y toma la primera parte de la clave.
                    """
                    self.new(eval("{}".format(class_name))(**value))
                    """Esta declaración if se utiliza para crear un nuevo
                    objeto con el nombre de clase de new_object y su valor
                    """
        except FileNotFoundError:
            pass
