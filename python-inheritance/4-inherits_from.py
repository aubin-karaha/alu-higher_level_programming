#!/usr/bin/python3
"""Module that defines a function to check strict inheritance."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class that inherits from
    a_class, but is not a_class itself.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
