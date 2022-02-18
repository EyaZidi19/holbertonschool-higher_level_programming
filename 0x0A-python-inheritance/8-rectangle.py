#!/usr/bin/python3
"""The module have a class that inherits
from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class rectangle
    arg: only init method"""

    def __init__(self, width, height):
        """Init method; width, height
        validation with integer_validator first"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
