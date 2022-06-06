import unittest
from sort import naive


test_ext = [
    (None, []),
    ([0], [0]),
    ([-10, 500, -11, -12, -11, -10], [-12, -11, -11, -10, -10, 500]),
]


class sort_test(unittest.TestCase):
    def test_integer_to_digits(self):
        for serie, expected in test_ext:
            with self.subTest(f"input = {serie}"):
                actual = naive(serie)
                self.assertListEqual(actual, expected)