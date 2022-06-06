import unittest
from bin_num import bin_to_num


test_ext = [
    (None, None),
    ([0], 0),
    ([1,1], 3),
    ([1,0,0,0], 8),
    ([1,0,1,1], 11),
]


class bin_num_test(unittest.TestCase):
    def test_integer_to_digits(self):
        for series,  expected in test_ext:
            with self.subTest(f"input = {series}"):
                actual = bin_to_num(series)
                self.assertEqual(actual, expected)