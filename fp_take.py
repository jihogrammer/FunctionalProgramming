from typing import Iterable, TypeVar

_T = TypeVar("_T")


def _take(length: int, _iter: Iterable[_T]) -> Iterable[_T]:
    result = []
    for item in _iter:
        result.append(item)
        if len(result) == length:
            return result
    return result
