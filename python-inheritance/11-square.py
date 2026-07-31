#!/usr/bin/python3
"""Module that defines a Square class with its own string description."""
Rectangle = __import__('10-square').Square.__bases__[0]


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: the size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return the printable description of the square."""
        return "[Square] {}/{}".format(
            self._Rectangle__width, self._Rectangle__height)
