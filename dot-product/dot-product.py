import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    x_arry  = np.asarray(x, dtype= float)
    y_arry  = np.asarray(y, dtype= float)

    return float(np.dot(x_arry,y_arry))