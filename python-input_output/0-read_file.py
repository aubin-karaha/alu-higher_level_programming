#!/usr/bin/python3
"""Module that defines a function to read and print a file's content."""


def read_file(filename=""):
    """Read a text file and print its contents to stdout.

    Args:
        filename: the path of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
