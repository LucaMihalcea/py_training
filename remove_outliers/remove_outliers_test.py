import unittest
from remove_outliers import *

test_ext = [
    (None, 12, []),
    ([0], 1, [0]),
    ([-10, 500, -11, -12, -11, -10], 50, [-12, -11, -11, -10, -10]),
]


class remove_outliers_test(unittest.TestCase):
    def test_integer_to_digits(self):
        for serie, p, expected in test_ext:
            with self.subTest(f"input = {serie}"):
                actual = remove_outliers(serie, p)
                self.assertListEqual(actual, expected)


median_nominal_cases = [
    ([0], (0, 0)),
    ([-10, 500, -11, -12, -11, -10], (3, -10)),
]

median_error_cases = [
    None,
    []
]


class MedianTests(unittest.TestCase):
    def test_nominal_cases(self):
        for serie, expected in median_nominal_cases:
            with self.subTest(f"input = {serie}"):
                actual = median(serie)
                self.assertTupleEqual(actual, expected)

    def test_error_cases(self):
        for serie in median_error_cases:
            with self.subTest(f"input = {serie}"):
                self.assertRaises(ValueError, lambda: median(serie))
