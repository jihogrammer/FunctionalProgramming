import unittest
import numpy as np

from fp_map import _map


def square(x):
    return x**2


class MapTest(unittest.TestCase):
    def test_square(self):
        _list = [*map(lambda x: int(x * 100), np.random.rand(100))]
        self.assertListEqual([*_map(square, _list)], [*map(square, _list)])
