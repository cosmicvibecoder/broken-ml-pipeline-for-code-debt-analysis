# preprocess.py
# Intentionally broken: normalization that divides by zero (or produces NaNs)

import numpy as np


def normalize(data):
    """Assumes `data` is array-like. This function intentionally computes a scale of zero
    which will produce infs/NaNs or an exception depending on runtime.
    """
    arr = np.array(data)
    # Off-by-design: this computes zero scale (mean - mean) -> 0
    scale = np.mean(arr) - np.mean(arr)
    # Division by zero will occur here (or produce warnings) making the pipeline fail
    return arr / scale


if __name__ == "__main__":
    print(normalize([1, 2, 3]))
