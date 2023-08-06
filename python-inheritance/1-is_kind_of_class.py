"""A function that determines whether 
an object is exactly an instance of a 
specified class
"""
def is_kind_of_class(obj, a_class):
    """Function that determines instance of an object

    Args:
    obj: object
    a_class: specified class
    
    """
    if isinstance(obj,a_class):
        return True
    return False



