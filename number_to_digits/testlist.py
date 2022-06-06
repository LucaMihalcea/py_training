import unittest
from main import num_to_list


test_cases = [
    (None, []),
    (0, [0]),
    (-10, [1,0]),
    (1, [1]),
    (12, [1, 2]),
    (123, [1, 2, 3]),
    (754213, [7, 5, 4, 2, 1, 3])
]


class DigitsOfIntegerTests(unittest.TestCase):
    def test_integer_to_digits(self):
        for src, expected in test_cases:
            with self.subTest(f"input = {src}"):
                actual = num_to_list(src)
                self.assertListEqual(actual, expected)

