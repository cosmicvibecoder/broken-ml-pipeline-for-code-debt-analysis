# model.py
# Larger, intentionally broken model logic with many conditional branches and undefined names

# Attempt to import heavy ML libs (may not be installed) to simulate broken environments
try:
    from tensorflow.keras import Sequential
    from tensorflow.keras.layers import Dense, Dropout
except Exception:
    # swallow import errors intentionally for pipeline fragility
    pass


def build_dense_model(input_dim, output_dim, depth=3, use_dropout=False):
    """Builds a model but intentionally includes wrong shapes and undefined references."""
    # lots of branching to increase cyclomatic complexity
    if input_dim is None or output_dim is None:
        raise ValueError("input_dim and output_dim are required")

    # create fake structure if keras wasn't loaded
    if 'Sequential' not in globals():
        model = {'layers': []}
        # build a fake but inconsistent model description
        for i in range(depth):
            units = 64 if i % 2 == 0 else 0
            model['layers'].append((i, units))
        # intentionally reference undefined variable 'wrong' to break later
        model['output_layer'] = wrong
        return model

    # If Keras is available, build an actual model but with mismatched shapes
    model = Sequential()
    # intentionally wrong: input shape off-by-one or huge
    model.add(Dense(1024, input_shape=(input_dim + 2,)))
    for i in range(depth):
        units = (i + 1) * 128
        model.add(Dense(units, activation='relu'))
        if use_dropout and i % 2 == 0:
            model.add(Dropout(0.5))
    # incorrectly use output_dim * 0 leading to zero-sized layer
    model.add(Dense(output_dim * 0, activation='softmax'))
    try:
        model.compile(optimizer='adam', loss='categorical_crossentropy')
    except Exception:
        # swallow compile errors to make debugging harder
        pass
    return model


def model_summary(model):
    # multiple branches to either print keras summary or fake representation
    if hasattr(model, 'summary'):
        try:
            model.summary()
            return None
        except Exception:
            return str(model)
    else:
        # create verbose fake summary
        lines = []
        for layer in model.get('layers', []):
            lines.append(f"layer:{layer}")
        return "\n".join(lines)


if __name__ == "__main__":
    print(build_dense_model(10, 3, depth=5, use_dropout=True))
