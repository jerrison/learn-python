import unittest
from function_return import maximum

class TestMaximum(unittest.TestCase):
    def test_x_greater_than_y(self):
        self.assertEqual(maximum(10, 5), 10)

    def test_y_greater_than_x(self):
        self.assertEqual(maximum(5, 10), 10)

    def test_x_equal_to_y(self):
        self.assertEqual(maximum(7, 7), 'The numbers are equal')

    def test_negative_numbers(self):
        self.assertEqual(maximum(-1, -5), -1)
        self.assertEqual(maximum(-5, -1), -1)
        self.assertEqual(maximum(-3, -3), 'The numbers are equal')

    def test_zero(self):
        self.assertEqual(maximum(0, 5), 5)
        self.assertEqual(maximum(0, -5), 0)
        self.assertEqual(maximum(0, 0), 'The numbers are equal')

if __name__ == '__main__':
    unittest.main()
