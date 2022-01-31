#!/usr/bin/python3
"""The module have one function to prove that
it is the object exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """Return True if the obj id exactly and
    instace of the a_class"""
    if type(obj) is a_class:
        return True
    return False
