import unittest
from num_bin import num_to_bin


test_ext = [
    (None, []),
    (0, [0]),
    (3, [1,1]),
    (8, [1,0,0,0]),
    (11, [1,0,1,1])
]


class num_bin_test(unittest.TestCase):
    def test_integer_to_digits(self):
        for series,  expected in test_ext:
            with self.subTest(f"input = {series}"):
                actual = num_to_bin(series)
                self.assertListEqual(actual, expected)