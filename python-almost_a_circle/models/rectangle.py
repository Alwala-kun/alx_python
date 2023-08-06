"""Module defining the base class for all other classes."""
class Base:


    """Defining a base class for all other classes
    Attributes:
        __nb_objects (int): int value
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing the base class.
        Args:
            id (int): gives an integer value"""
        if id is not None:
            self.id = id
        else :
            Base.__nb_objects+=1
            self.id = Base.__nb_objects


class Rectangle(Base):
    """Class rectangle inherits from base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor to initialize rectangle"""
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
    def x_value(self):
         return self.__x
     
    @x_value.setter
    def x_value(self,value):
         self.__x = value

    @property
    def y_value(self):
         return self.__y
     
    @y_value.setter
    def y_value(self, value):
         self.__y = value



    


 


     
    

    