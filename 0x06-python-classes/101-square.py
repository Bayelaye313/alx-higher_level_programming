#!/usr/bin/python3

class Square:
    """Square class with size and position attributes."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize data."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get size."""
        return self.__size

    @property
    def position(self):
        """Get position."""
        return self.__position

    @size.setter
    def size(self, value):
        """Set size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """Set position."""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(coord, int) and coord >= 0 for coord in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Get area of the square."""
        return self.size ** 2

    def my_print(self):
        """Print the square."""
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
