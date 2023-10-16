#!/usr/bin/puthon3
"""Implementation of the Placeclass, which inherits from the BaseModel class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Class definition of the Place Class"""
    city_id = ""
    user_id = ""
    name = ""
    description = 0
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
