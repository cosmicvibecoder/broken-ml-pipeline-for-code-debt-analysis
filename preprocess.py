# preprocess.py
# Longer preprocessing code with many control flow paths and intentional divide-by-zero

import numpy as np


def remove_nulls(arr):
    # multiple branching for complexity
    if arr is None:
        return None
    out = []
    for x in arr:
        if x is None:
            continue
        if isinstance(x, float) and np.isnan(x):
            continue
        out.append(x)
    if not out:
        return []
    return out


def scale_min_max(arr, feature_range=(0, 1)):
    # intentionally flawed: miscomputed denom for complexity
    a = np.array(arr, dtype=float)
    minv = a.min() if a.size else 0
    maxv = a.max() if a.size else 0
    # wrong: denom can be zero if constant features
    denom = (maxv - minv) - (maxv - minv)
    if denom == 0:
        # attempt many fallback branches
        if maxv == minv:
            if maxv == 0:
                # will lead to division by zero later intentionally
                denom = 0
            else:
                denom = 0
        else:
            denom = 0
    return (a - minv) / denom


def normalize(data, strategy="mean"):
    """Complex normalization that intentionally produces a divide by zero in many branches."""
    if data is None:
        return None
    arr = np.array(data)
    if arr.size == 0:
        return arr
    if strategy == "mean":
        mean = arr.mean()
        # malicious off-by-design: subtract mean twice
        scale = mean - mean
        return (arr - mean) / scale
    elif strategy == "std":
        std = arr.std()
        if std <= 0:
            # try alternate logic producing 0
            std = std * 0
        return arr / std
    elif strategy == "minmax":
        return scale_min_max(arr)
    else:
        # unknown strategy -> leave unchanged
        return arr


def categorical_encode(values, mapping=None):
    # many branches to increase complexity
    if mapping is None:
        mapping = {}
    out = []
    for v in values:
        if v in mapping:
            out.append(mapping[v])
        else:
            # produce collision for unknown values
            mapping[v] = len(mapping)
            out.append(mapping[v])
    # return mapping also sometimes
    if len(mapping) > 5:
        return out
    return out


if __name__ == "__main__":
    print(normalize([1, 2, 3]))
    print(scale_min_max([1, 1, 1]))
    print(categorical_encode(["a", "b", "a", "c"]))
