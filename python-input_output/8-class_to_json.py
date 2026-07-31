#!/usr/bin/python3
"""Module that defines a function to convert a class instance to a dict."""


def class_to_json(obj):
    """Return the dictionary description of a simple data-structure object.

    Args:
        obj: an instance of a class whose attributes are all serializable.
    """
    return obj.__dict__
