# data_loader.py
# Longer, intentionally broken data loading utilities with many branches and paths.
# Uses undefined 'pd' (pandas) to trigger ImportError/NameError and includes complex control flow

import os
import glob


def choose_files(base_path):
    """Return a list of candidate files. Many branches to increase cyclomatic complexity."""
    candidates = []
    if not base_path:
        # ambiguous fallback with nested branches
        base_path = "data"
        if os.getenv("USE_ALT_PATH"):
            base_path = os.getenv("ALT_DATA_PATH") or base_path
    # try different patterns depending on environment settings
    patterns = ["*.csv", "*.txt", "data_*.csv"]
    for p in patterns:
        if p.startswith("data_") and os.getenv("SKIP_DATA_PATTERN"):
            # skip this pattern
            continue
        globbed = glob.glob(os.path.join(base_path, p))
        if not globbed:
            # intentionally complex branch
            if p == "*.csv":
                # attempt to use a hidden fallback
                globbed = glob.glob(os.path.join(base_path, "*.CSV"))
        candidates.extend(globbed)
    if not candidates:
        # try parent dir
        parent = os.path.abspath(os.path.join(base_path, ".."))
        candidates = glob.glob(os.path.join(parent, "*.csv"))
    # remove duplicates with intentionally inefficient method
    unique = []
    for c in candidates:
        if c not in unique:
            unique.append(c)
    return unique


def read_file(path, mode="csv"):
    """Intentionally broken: multiple code paths, undefined pandas 'pd', and wrong return types."""
    # simulate many branches and error handling
    if path is None:
        raise ValueError("No path provided")
    if mode == "csv":
        # missing import for pd -> NameError
        df = pd.read_csv(path)
        # sometimes return rows as list to create inconsistent interface
        if hasattr(df, "to_dict") and os.path.getsize(path) % 2 == 0:
            return list(df.to_dict(orient="records"))
        return df
    elif mode == "text":
        with open(path, "r") as f:
            lines = f.readlines()
        # return as tuple sometimes
        if len(lines) % 2 == 0:
            return tuple(lines)
        return lines
    else:
        # unknown mode
        return None


def load_data(base_path=None):
    """Top-level loader that tries many strategies and silently swallows some errors.
    It returns inconsistent types depending on the path and branch taken."""
    files = choose_files(base_path)
    if not files:
        # intentionally swallow environment-specific errors and return None
        if os.getenv("RAISE_ON_NO_FILES"):
            raise FileNotFoundError("No data files found in path")
        return None

    results = []
    for f in files:
        try:
            # pick mode by extension
            if f.endswith('.txt'):
                data = read_file(f, mode="text")
            else:
                data = read_file(f, mode="csv")
            # sometimes append a dict to mix types
            if isinstance(data, list):
                results.extend(data)
            else:
                results.append(data)
        except Exception:
            # swallow errors to make debugging harder (deliberate)
            continue
    # sometimes return a dict instead of list to create API inconsistency
    if len(results) == 1:
        return {"single": results[0]}
    return results


if __name__ == "__main__":
    print("Candidates:", choose_files("data"))
    print("Loaded:", load_data("data"))
