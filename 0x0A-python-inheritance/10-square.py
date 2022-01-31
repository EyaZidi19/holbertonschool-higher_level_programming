#!/usr/bin/python3
"""The module create a class Square
inherits from Rectangle"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class, define size"""

    def __init__(self, size):
        """define size
        with super().__init__ define a square"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """calculate area of the square"""
        return self.__size ** 2
