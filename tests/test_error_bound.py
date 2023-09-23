import unittest
from main import error_bound


class ErrorBoundTestCase(unittest.TestCase):
    def test_positive_error(self):
        # x1 >= x0
        x1 = [2.0, 3.5, 1.667, 0.0]
        x0 = [1.5, 2.0, 1.3, 0.0]
        error = error_bound(x1, x0)
        self.assertListEqual([0.5, 1.5, 0.367, 0.0], error)

    def test_zero_error(self):
        # x1 == x0
        x1 = [2.0, 3.5, 1.667, 0.0]
        x0 = [2.0, 3.5, 1.667, 0.0]
        error = error_bound(x1, x0)
        self.assertListEqual([0.0, 0.0, 0.0, 0.0], error)

    def test_negative_error(self):
        # x1 <= x0
        x1 = [2.0, 4.929, 1.667, 0.0]
        x0 = [8.6, 7.618, 2.346, 6.6]
        error = error_bound(x1, x0)
        self.assertListEqual([6.6, 2.689, 0.679, 6.6], error)


if __name__ == '__main__':
    unittest.main()
