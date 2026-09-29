import unittest

from calculator import (
    add, subtract, multiply, divide, power, is_even, factorial, average
)


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(1, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(7))

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_average(self):
        self.assertEqual(average([2, 4, 6]), 4)

    def test_average_empty(self):
        with self.assertRaises(ValueError):
            average([])


if __name__ == "__main__":
    unittest.main()
