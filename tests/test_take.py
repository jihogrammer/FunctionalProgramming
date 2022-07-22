import unittest
import numpy as np

from fp_take import _take


class TakeTest(unittest.TestCase):
    def test_take_10(self):
        _list = [*map(lambda x: int(x * 100), np.random.rand(100))]
        self.assertEqual(10, len(_take(10, _list)))
        self.assertListEqual(_list[:10], _take(10, _list))
