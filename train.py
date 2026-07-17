# train.py
# Intentionally broken training loop: uses undefined variables, swallows exceptions, and mixes APIs

from data_loader import load_data
from preprocess import normalize
from model import build_model


def train():
    # load_data returns a DataFrame (or raises) — downstream code expects numeric arrays
    data = load_data()

    # normalize expects array-like; if data is None or a DataFrame this will error
    X = normalize(data)

    # Attempt to build model with wrong dimensions; may raise
    model = build_model(X.shape[1], 10)

    try:
        # Undefined 'y' variable; train_on_batch may not exist depending on model object
        for epoch in range(5):
            loss = model.train_on_batch(X, y)
            print("Epoch", epoch, "loss", loss)
    except Exception:
        # Swallow all exceptions silently — makes debugging impossible and hides failures
        pass


if __name__ == "__main__":
    train()
