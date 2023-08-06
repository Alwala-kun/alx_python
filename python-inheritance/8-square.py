"Defining an empty class"
class BaseGeometry:
    "Defining an empty class"

    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if type(value)!= int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        

class Rectangle(BaseGeometry):
    """Represents a rectangle using base geometry"""
    def __init__(self, width, height):
        """Initialize a new rectangle
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    
    def area(self):
        """Calculate area of rectangle"""
        return self.__height * self.__width
    
    

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
    

class Square(Rectangle):
    """Represents a square using rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size,size)
        self.__size = size

    def area(self):
        return self.__size ** 2
    


