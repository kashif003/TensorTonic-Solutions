from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    mean = float(np.mean(x))
    median = float(np.median(x))
    count = Counter(x)
    sorted_cont = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))

    
    return {"mean":mean, "median":median, "mode":float(next(iter(sorted_cont)))}

