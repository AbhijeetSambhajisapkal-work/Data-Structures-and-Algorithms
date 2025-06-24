def declare(Size:int):
    """
    This function declares a variable with the given size.
    
    Parameters:
    Size (int): The size of the variable to declare.
    
    Returns:
    None
    """
    # Declare a variable with the specified size
    variable = [0] * Size;
    print(f"Declared a variable of size {Size}: {variable}")
    return variable;

def declare():
    """
    This function declares a variable with a default size of 10.
    
    Returns:
    None
    """
    # Declare a variable with the default size
    variable = [];
    varibale2 = list();
    print(f"Declared a variable of size 10: {variable}")
    return variable;

def declareEmpty2Dlist():
    """
    This function declares a 2D array with default values or empty 2D array

    Returns:
    None
    """

    #Declare the variable with default size
    arr_2d = []
    print(f"Declared an empty 2D array: {arr_2d}")
    return arr_2d



def declareZeros2DList(rows=3,cols=1):
    """
    
    This function declares a 2D array with the given number of rows,
    each initialized with zeros (default columns = 0).
    
    """
    arr_2d = [[0 for _ in range(cols)] for _ in range(rows)]
    print(f"Declared a 2D array with {rows} rows and {cols} columns (all zeros): {arr_2d}")
    return arr_2d


