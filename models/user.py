#!/usr/bin/env python3
""" Class User """
from models.base_model import BaseModel

class User(BaseModel):
    """ Class user that inherits from BaseModel
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
                *args: list of strings
                **kwargs: dictionary of strings
                """
        super().__init__(*args, **kwargs)
