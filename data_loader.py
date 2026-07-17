# data_loader.py
# Intentionally broken: uses pandas without importing it and points to a nonexistent path.

def load_data(path="data/nonexistent.csv"):
    # This will raise NameError because pd is not defined, and FileNotFoundError if path existed
    df = pd.read_csv(path)
    # Return something inconsistent (a DataFrame when other code expects numpy arrays)
    return df


if __name__ == "__main__":
    print("Loaded:", load_data())
