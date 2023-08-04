"""
This module defines the Square class, which represents a square with a private instance attribute 'size'.
"""
class Square:
    """
    Square class represents a square with a private instance attribute 'size'.
    """
    def __init__(self,size=0):
        """
        Constructor for Square class.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size,int):
            raise TypeError("size must be an integer")
        
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size


    def area(self):
        """Finding the area of the square."""
        square_area = self.__size **2
        return square_area
    
    @property
    def size(self):
        """Getting the size of the square"""
        return self.__size
    
    @size.setter
    def size(self,value):
        """Setting the value of the size of the square.

        Args:
            value(int):The new value of the square.
        """
        if not isinstance(value,int):
            raise TypeError("size must be an integer")
        
        if value < 0:
            raise ValueError("size must be >=0")
        
        self.__size = value

    
    def my_print(self):
        """Printing in stdout the square"""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#"* self.__size)


