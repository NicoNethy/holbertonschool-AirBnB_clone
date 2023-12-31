#!/usr/bin/env python3
""" Class place"""
from models.base_model import BaseModel


class State(BaseModel):
    """ Class place that inherits from BaseModel
        Atributos de clase Publicos:
            name: (str) - Nombre del state
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize class attributes
            Args:
            *args: list of strings
           **kwargs: dictionary of strings
        """
        super().__init__(*args, **kwargs)
