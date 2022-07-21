from typing import Any, Callable, Iterable, TypeVar

_iter = [1, 2, 3, 4, 5]


def is_even(x: int) -> int:
    return x & 1


_T = TypeVar("_T")


def _filter(f: Callable[[_T], Any], __iter: Iterable[_T]):
    for x in __iter:
        if f(x):
            yield x


a = [*filter(is_even, _iter)]
b = [*_filter(is_even, _iter)]

print("DEFAULT", a)
print("FUNCTIONAL", b)

for x, y in zip(a, b):
    assert x == y

print("! SAME RESULT !")
