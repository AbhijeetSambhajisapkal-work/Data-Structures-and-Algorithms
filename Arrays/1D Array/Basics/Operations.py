def insert_at_index(lst, index, value):
    """
    Inserts a value at a specific index in a list.
    
    :param lst: List to insert into
    :param index: Index at which to insert the value
    :param value: Value to insert
    :return: None (the list is modified in place)
    """
    lst.insert(index, value);

    ''' 

    lst[index] = value;

    '''

def remove_at_index(lst, index):
    """
    Removes the value at a specific index from a list.
    
    :param lst: List to remove from
    :param index: Index of the value to remove
    :return: None (the list is modified in place)
    """
    if 0 <= index < len(lst):
        del lst[index]
    else:
        raise IndexError("Index out of range")

def replace_at_index(lst, index, value):
    """
    Replaces the value at a specific index in a list with a new value.
    
    :param lst: List to modify
    :param index: Index of the value to replace
    :param value: New value to insert
    :return: None (the list is modified in place)
    """
    if 0 <= index < len(lst):
        lst[index] = value
    else:
        raise IndexError("Index out of range")


def get_value_at_index(lst, index):
    """
    Retrieves the value at a specific index in a list.
    
    :param lst: List to retrieve from
    :param index: Index of the value to retrieve
    :return: Value at the specified index
    """
    if 0 <= index < len(lst):
        return lst[index]
    else:
        raise IndexError("Index out of range")

def get_length(lst): 
    """
    Returns the length of the list.
    
    :param lst: List to get the length of
    :return: Length of the list
    """
    return len(lst)