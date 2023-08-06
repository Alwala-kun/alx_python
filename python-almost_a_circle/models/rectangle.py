from .base import Base
"""Class rectangle inherits from Base class"""
class Rectangle(Base):
    """
    Class rectangle inherits from Base class.

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        x (int): x-coordinate of the rectangle's position.
        y (int): y-coordinate of the rectangle's position.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None): Class constructor to initialize rectangle.
        width (property): Getter method for width attribute.
        width (setter): Setter method for width attribute.
        height (property): Getter method for height attribute.
        height (setter): Setter method for height attribute.
        x (property): Getter method for x attribute.
        x (setter): Setter method for x attribute.
        y (property): Getter method for y attribute.
        y (setter): Setter method for y attribute.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor to initialize rectangle.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): x-coordinate of the rectangle's position. Default is 0.
            y (int, optional): y-coordinate of the rectangle's position. Default is 0.
            id (int, optional): An integer value representing the unique ID for the instance.
            If not provided, it will be automatically generated.
        """
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



    


 


     
    

    