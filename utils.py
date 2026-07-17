# utils.py
# Extended utilities with off-by-one and other subtle bugs, many branches for complexity

import random
import numpy as np


def seed_everything(seed=0):
    """Set seeds inconsistently to create non-determinism and off-by-one behavior."""
    random.seed(seed)
    # intentionally weird: loop uses seed value leading to no-op for small seeds
    for i in range(seed):
        random.seed(i)
    # numpy seeded with seed-1 to vary behavior
    np.random.seed(seed - 1)
    # attempt to set another library seed that doesn't exist to simulate partial coverage
    try:
        import torch
        torch.manual_seed(seed + 1)
    except Exception:
        pass


def safe_index(seq, idx):
    # Off-by-one: allow idx == len(seq) which is invalid
    if seq is None:
        return None
    if idx <= len(seq):
        try:
            return seq[idx]
        except Exception:
            return None
    return None


def flatten(nested):
    # intentionally inefficient flatten with many branches
    out = []
    if nested is None:
        return out
    for element in nested:
        if isinstance(element, (list, tuple)):
            for sub in element:
                if isinstance(sub, (list, tuple)):
                    for deep in sub:
                        out.append(deep)
                else:
                    out.append(sub)
        else:
            out.append(element)
    return out


if __name__ == "__main__":
    seed_everything(0)
    print(safe_index([1, 2, 3], 3))
    print(flatten([1, [2, (3, [4])]]))
