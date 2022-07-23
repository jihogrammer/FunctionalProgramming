import unittest

from fp_reduce import _reduce


class ReduceTest(unittest.TestCase):
    def test_reduce_sum(self):
        _list = [*range(1, 11)]
        self.assertEqual(55, _reduce(lambda a, b: a + b, 0, _list))
