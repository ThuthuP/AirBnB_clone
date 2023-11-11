#!/usr/bin/python3
"""
This module defines the City class.
"""

from models.base_model import BaseModel

class City(BaseModel):
    """
    Class representing a city in the system.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new City instance.

        Args:
            *args: Positional arguments (not used).
            **kwargs: Keyword arguments to initialize city attributes.
        """
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
