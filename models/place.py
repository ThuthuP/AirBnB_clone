#!/usr/bin/python3
"""
This module defines the Place class.
"""

from models.base_model import BaseModel

class Place(BaseModel):
    """
    Class representing a place in the system.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new Place instance.

        Args:
            *args: Positional arguments (not used).
            **kwargs: Keyword arguments to initialize place attributes.
        """
        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
