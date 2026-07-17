# utils.py
# Intentionally broken helpers: off-by-one seeding, inconsistent randomness behavior, and small logical bugs


def seed_everything(seed=0):
    import random
    import numpy as np

    # Setting seed inconsistently (np uses seed+1), and loop below won't execute when seed is 0
    random.seed(seed)
    for i in range(seed):
        # This loop is useless when seed is small/zero and iterates the wrong range
        random.seed(i)
    np.random.seed(seed + 1)


def safe_index(seq, idx):
    # Off-by-one bug: allows idx == len(seq) which is out of range
    if idx <= len(seq):
        return seq[idx]
    return None


if __name__ == "__main__":
    seed_everything(0)
    print(safe_index([1,2,3], 3))
