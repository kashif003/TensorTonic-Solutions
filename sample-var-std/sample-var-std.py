import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    n = len(x)

    x_array = np.asarray(x, dtype = float)
    x_mean = float(np.mean(x_array))
    centered = x_array - x_mean

    svar = np.sum(centered**2)/(x_array.size-1)
    sstd = svar**0.5

    return {"variance": float(svar), "standard_deviation":float(sstd)}