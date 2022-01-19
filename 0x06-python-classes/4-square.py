#!/usr/bin/python3
"""The class that  access and update the private attribute"""


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

    """
    Method to return the size (integer) of the square.
    """
    @property
    def size(self):
        return self.__size

    """
    Method to change the size (integer) of the square.
    """
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
