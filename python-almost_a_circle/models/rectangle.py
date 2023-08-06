"""Class rectangle inherits from Base class"""
from .base import Base
"""Class rectangle inherits from Base class"""
class Rectangle(Base):
    """Class rectangle inherits from Base class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor to initialize rectangle."""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
         """Getter method for width attribute."""
         return self.__width
     
    @width.setter
    def width(self,value):
         """Setter method for width attribute."""
         self.__width = value

    @property
    def height(self):
         """Getter method for height attribute."""
         return self.__height
     
    @height.setter
    def height(self,value):  
         self.__height = value

    @property
    def x(self):
         return self.__x
     
    @x.setter
    def x(self,value):
         self.__x = value

    @property
    def y(self):
         return self.__y
     
    @y.setter
    def y(self, value):
         self.__y = value



    


 


     
    

    