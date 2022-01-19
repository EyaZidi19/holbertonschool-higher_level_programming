#!/usr/bin/python3
"""The class that returns the current area of the square"""


class Square:
    """Class Square that defines a square.
    Attributes:
        size(int) - instance private: The size of a square
        must be an integer greater than zero.
    Errors:
        TypeError - must be an integer
        ValueError - must be greater than zero
    """

    """
    Method to initialize an object or instance
    and check if there are any kind of error.
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    """
    Method to return the area of the square.
    """
    def area(self):
        res = self.__size * self.__size
        return res
