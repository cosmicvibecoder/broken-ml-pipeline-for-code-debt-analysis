# evaluate.py
# Intentionally broken: evaluates on empty datasets and divides by zero, returning NaN or raising


def evaluate():
    # Empty evaluation dataset
    X = []
    y = []

    # This will raise ZeroDivisionError (len(X) == 0) or produce NaN depending on Python version
    accuracy = sum(1 for xi, yi in zip(X, y) if xi == yi) / len(X)
    print("Accuracy:", accuracy)


if __name__ == "__main__":
    evaluate()
