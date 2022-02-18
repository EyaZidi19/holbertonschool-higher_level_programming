#!/usr/bin/python3
"""The module have a vacue class"""


class BaseGeometry:
    """empty class BaseGeometry
    arg:
        public method: area"""

    def area(self):
        """public method, calculate the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
