#!/usr/bin/python3
"""The  module have a Class
that inherist from list
"""


class MyList(list):
    """This class sorted the list
    arg:
        public method: print_sorted
    """
    def print_sorted(self):
        """Use sorted to sort the list"""
        print(sorted(self))
