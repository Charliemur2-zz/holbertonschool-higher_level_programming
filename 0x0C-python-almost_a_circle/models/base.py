#!/usr/bin/python3
"""
class Base
Created: June 06, 2020
By: Carlos Murcia
"""


class Base:
    """
    class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor.
        atributes:
        id: integer from id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects