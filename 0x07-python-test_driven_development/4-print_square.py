#!/usr/bin/python3
""" this is the Square-printing module """


def print_square(size):
    """func to prints a square with #s """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for i in range(size):
            print("#", end="")
        print()
