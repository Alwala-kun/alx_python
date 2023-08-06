"""A function that determines whether 
an object is exactly an instance of a 
specified class
"""
def is_same_class(obj, a_class):
    """Function that determines instance of an object

    Args:
    obj: object
    a_class: specified class
    
    """
    if type(obj) is a_class:
        return True
    return False



