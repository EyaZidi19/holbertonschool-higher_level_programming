#!/usr/bin/python3
"""The class that returns the current square area of the square """


class Square:

    """
    Class Square that defines a square.
    Attributes:
    size(int) - instance private: The size of a square
    must be an integer greater than zero.
    def area(self): - Public instance method: returns the 
    current square area 
    Errors:
    TypeError - must be an integer
    ValueError - must be greater than zero 
    """

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
     
    def area(self):
        res = self.__size * self.__size
        return res
