"""A function that determines whether
an object is exactly an child class of a
specified class
"""
def inherits_from(obj, a_class):


    """Function that determines inheritance.Args:
obj: object a_class: specified class"""
    obj_class = type(obj)
    if issubclass(obj_class, a_class) and obj_class != a_class:
        return True
    return False
