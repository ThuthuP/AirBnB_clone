#!/usr/bin/python3
"""
This module defines the Amenity class.
"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    Class representing an amenity in the system.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new Amenity instance.

        Args:
            *args: Positional arguments (not used).
            **kwargs: Keyword arguments to initialize amenity attributes.
        """
        super().__init__(*args, **kwargs)
        self.name = ""
