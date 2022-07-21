import unittest
import numpy as np

from fp_filter import _filter


def is_even(x: int) -> int:
    return x & 1


class FilterTest(unittest.TestCase):
    def test_is_even(self) -> None:
        _list = [1, 2, 3, 4, 5]
        self.assertListEqual([*_filter(is_even, _list)], [1, 3, 5])

    def test_is_even_random(self):
        _list = [*map(lambda x: int(x * 100), np.random.rand(100))]
        self.assertListEqual([*_filter(is_even, _list)], [*filter(is_even, _list)])
