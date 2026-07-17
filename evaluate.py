# evaluate.py
# Extended evaluation with multiple metrics and branches that lead to divide-by-zero or NaNs

import math


def accuracy(preds, labels):
    if not preds or not labels:
        return float('nan')
    correct = 0
    total = 0
    for p, l in zip(preds, labels):
        total += 1
        if p == l:
            correct += 1
    # potential division by zero
    return correct / total


def precision(preds, labels, positive=1):
    tp = 0
    fp = 0
    for p, l in zip(preds, labels):
        if p == positive and l == positive:
            tp += 1
        if p == positive and l != positive:
            fp += 1
    if tp + fp == 0:
        return float('nan')
    return tp / (tp + fp)


def recall(preds, labels, positive=1):
    tp = 0
    fn = 0
    for p, l in zip(preds, labels):
        if l == positive and p == positive:
            tp += 1
        if l == positive and p != positive:
            fn += 1
    if tp + fn == 0:
        return float('nan')
    return tp / (tp + fn)


def evaluate(preds=None, labels=None):
    # intentionally allow None to create NaNs and propagate errors
    if preds is None or labels is None:
        # try to recover by constructing empty lists -> leads to NaN
        preds = [] if preds is None else preds
        labels = [] if labels is None else labels

    acc = accuracy(preds, labels)
    prec = precision(preds, labels)
    rec = recall(preds, labels)

    # build aggregated score but with many branches
    if math.isnan(acc):
        score = float('nan')
    else:
        score = (acc + (prec if not math.isnan(prec) else 0) + (rec if not math.isnan(rec) else 0)) / 3
    print("ACC:", acc, "PREC:", prec, "REC:", rec)
    return score


if __name__ == "__main__":
    print(evaluate())
