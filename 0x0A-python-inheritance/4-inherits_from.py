#!/usr/bin/python3
"""
The function that returns True
if the object is an instance of a class that inherited
(directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """True if the obj inherited"""
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    return False
