#!/usr/bin/env python3
""" Clase User """
from models.base_model import BaseModel


class User(BaseModel):
    """ Clase user que hereda de BaseModel

    Atributos de clase publicos:
        first_name: (str) - user's first name
        last_name: (str) - user's last name
        password: (str) - user's password
        email: (str) - user's email
    """

    first_name = ""
    last_name = ""
    password = ""
    email = ""

    def __init__(self, *args, **kwargs):
        """ Inicializar la clase Usuario

        Args:
            *args: lista de cadenas de texto
            **kwargs: diccionario de cadenas de texto
        """
        super().__init__(*args, **kwargs)

