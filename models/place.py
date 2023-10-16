<<<<<<< HEAD
#!/usr/bin/puthon3
"""Implementation of the Placeclass, which inherits from the BaseModel class"""
=======
#!/usr/bin/python3
"""Defines Place class
"""
>>>>>>> 36fed9804ee6d657028ca0615f66e8c655736430
from models.base_model import BaseModel


class Place(BaseModel):
<<<<<<< HEAD
    """Class definition of the Place Class"""
    city_id = ""
    user_id = ""
    name = ""
    description = 0
=======
    """Place class  saves the attributes of an place:
        - city_id (string)
        - user_id string)
        - name (string)
        - description (string)
        - number_rooms (integer)
        - number_bathrooms (integer)
        - max_guest (integer)
        - price_by_night (integer)
        - latitude (float)
        - longitude (float)
        - amenity_ids (list of strings)
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
>>>>>>> 36fed9804ee6d657028ca0615f66e8c655736430
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
