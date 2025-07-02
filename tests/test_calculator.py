import unittest

from calculator import divide_numbers

class TestCalculator(unittest.TestCase):
    def test_divide_normal(self):
        self.assertEqual(divide_numbers(10, 2), 5)

    def test_divide_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide_numbers(1, 0)

if __name__ == '__main__':
    unittest.main()
