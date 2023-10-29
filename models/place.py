#!/usr/bin/env python3
"""" Class place """
from models.base_model import BaseModel


class Place(BaseModel):
   """ La clase Place hereda de BaseModel
    Atributos de clase públicos:
        city_id: string - (str): City.id
        user_id: string - (str): User.id
        number_bathrooms: (int) - Número de baños del lugar
        max_guest: (int) - Número máximo de huéspedes que se pueden alojar
        price_by_night: (int) - Precio por noche
        latitude: (float) - Latitud del lugar
        amenity_ids: (list) - Lista de Amenity.id
        name: (str) - Nombre del lugar
        longitude: (float) - Longitud del lugar
        description: (str) - Descripción del lugar
        number_rooms: (int) - Número de habitaciones del lugar
"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """ Initialize class Place
            Args:
                *args: list of strings
                **kwargs: dictionary of strings
                """
        super().__init__(*args, **kwargs)
