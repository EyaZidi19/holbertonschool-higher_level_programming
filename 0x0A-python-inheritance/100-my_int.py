#!/usr/bin/python3
"""Class MyInt that inherits from int."""


class MyInt(int):
    """invert int operators"""

    def __eq__(self, value):
        """Override equal opeartor with opposed behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override opposed operator with equal behavior."""
        return self.real == value
