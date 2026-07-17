# model.py
# Intentionally broken: malformed model definition with mismatched shapes and undefined variables.

# Note: importing tensorflow or keras may not even be available in the environment; that itself is part
# of the "broken pipeline" goal.
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense


def build_model(input_dim, output_dim):
    """Builds a model incorrectly: wrong input_shape and uses undefined variable 'wrong'.
    This will raise NameError or shape errors during training.
    """
    model = Sequential()
    # Wrong: input_dim+1 likely mismatches the data shape
    model.add(Dense(1000, input_shape=(input_dim + 1,)))
    # Wrong: 'wrong' is not defined anywhere
    model.add(Dense(wrong))
    model.compile(optimizer='adam', loss='mse')
    return model


if __name__ == "__main__":
    print("Model build attempted")
