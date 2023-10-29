#!/usr/bin/env python3
""" Class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ La clase Place hereda de BaseModel
    Atributos de clase públicos:
        city_id: string - (str): City.id
        user_id: string - (str): User.id
        name: (str) - Nombre del lugar
        description: (str) - Descripción del lugar
        number_rooms: (int) - Número de habitaciones del lugar
        number_bathrooms: (int) - Número de baños del lugar
        max_guest: (int) - Número máximo de huéspedes que se pueden alojar
        price_by_night: (int) - Precio por noche
        latitude: (float) - Latitud del lugar
        longitude: (float) - Longitud del lugar
        amenity_ids: (list) - Lista de Amenity.id
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ Initialize a Review instance
            Args:
                *args: list of strings
                **kwargs: dictionary of strings
        """
        super().__init__(*args, **kwargs)
