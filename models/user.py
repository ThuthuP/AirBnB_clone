#!/usr/bin/python3
"""This module defines the User class."""

from models.base_model import BaseModel

class User(BaseModel):
    """Class representing a user in the system."""

    def __init__(self, *args, **kwargs):
        """Initialize a new User instance.

        Args:
            *args: Positional arguments (not used).
            **kwargs: Keyword arguments to initialize user attributes.
        """
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
