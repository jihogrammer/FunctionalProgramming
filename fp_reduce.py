def _reduce(f, acc, _iter):
    for item in _iter:
        acc = f(acc, item)
    return acc
