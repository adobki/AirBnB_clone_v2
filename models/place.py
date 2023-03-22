#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel


class Place(BaseModel):
    """ A place to stay """
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
    # print("Place invoked!")

    def __init__(self, *args, **kwargs):
        """Call superclass init method to invoke inheritance of its methods."""
        if kwargs:
            # print('\nPlace kwargs', kwargs, '\n')
            for key in kwargs:
                if key != '__class__':
                    setattr(self, key, kwargs[key])
        super(Place, self).__init__(*args, **kwargs)
