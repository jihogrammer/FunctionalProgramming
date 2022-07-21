def _map(f, __iter):
    for x in __iter:
        yield f(x)
