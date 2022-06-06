import unittest
from remove_extrems import remove_ext


test_ext = [
    (None, 12 , []),
    ([0], 1, [0]),
    ([-10, 500, -11, -12, -11, -10], 50, [-12, -11, -11, -10, -10]),
]


class remove_ext_test(unittest.TestCase):
    def test_integer_to_digits(self):
        for serie, p,  expected in test_ext:
            with self.subTest(f"input = {serie}"):
                actual = remove_ext(serie,p)
                self.assertListEqual(actual, expected)