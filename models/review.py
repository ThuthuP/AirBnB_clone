#!/usr/bin/python3
"""
This module defines the Review class.
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """
    Class representing a review in the system.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new Review instance.

        Args:
            *args: Positional arguments (not used).
            **kwargs: Keyword arguments to initialize review attributes.
        """
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
