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