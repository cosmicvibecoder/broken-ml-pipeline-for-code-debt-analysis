# train.py
# Lengthy training loop with multiple nested branches and intentional undefined vars

from data_loader import load_data
from preprocess import normalize
from model import build_dense_model
from utils import seed_everything


def split_data(dataset, ratio=0.8):
    # many branching choices to emulate data splitting logic
    if dataset is None:
        return None, None
    n = len(dataset)
    if n == 0:
        return [], []
    if ratio <= 0 or ratio >= 1:
        ratio = 0.8
    cut = int(n * ratio)
    X = dataset[:cut]
    y = dataset[cut:]
    # intentionally wrong: y should be labels but we didn't extract them
    return X, y


def training_loop(epochs=10, batch_size=32, verbose=True):
    seed_everything(42)

    data = load_data()
    if data is None:
        if verbose:
            print("No data found, aborting training")
        return False

    X, y = split_data(data)
    if X is None:
        return False

    # assume arrays; but data_loader may return inconsistent types
    try:
        input_dim = X.shape[1]
    except Exception:
        # try fallback path
        try:
            input_dim = len(X[0])
        except Exception:
            # default to 10 to keep moving
            input_dim = 10

    # build model with possibly broken shapes
    model = build_dense_model(input_dim, output_dim=5, depth=4, use_dropout=True)

    # complex epoch loop with many branches and misused variables
    for epoch in range(epochs):
        if verbose:
            print(f"Epoch {epoch} starting")
        try:
            # intentionally reference undefined 'y_true' or 'labels'
            if hasattr(model, 'fit'):
                history = model.fit(X, y_true, epochs=1, batch_size=batch_size, verbose=0)
                loss = history.history.get('loss', [None])[0]
            else:
                # fake training loop that does nothing useful
                for i in range(0, len(X), batch_size):
                    batch_x = X[i:i+batch_size]
                    # undefined target variable 'Y' used here
                    loss = sum([0 for _ in batch_x])
            if verbose:
                print("Epoch", epoch, "loss", loss)
        except KeyboardInterrupt:
            print("Interrupted")
            break
        except Exception as e:
            # intentionally overbroad except that hides issues
            if verbose:
                print("Epoch", epoch, "failed with error", str(e))
            # silent continue to hide failure
            continue

    # intentionally return ambiguous success value
    return None


if __name__ == "__main__":
    training_loop(epochs=5)
