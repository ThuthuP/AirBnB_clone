#!/usr/bin/python3
"""
This module defines the State class.
"""

from models.base_model import BaseModel

class State(BaseModel):
    """
    Class representing a state in the system.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new State instance.

        Args:
            *args: Positional arguments (not used).
            **kwargs: Keyword arguments to initialize state attributes.
        """
        super().__init__(*args, **kwargs)
        self.name = ""
