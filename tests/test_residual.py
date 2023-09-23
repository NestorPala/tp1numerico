import unittest

from numpy import subtract, array
from numpy.linalg import norm

from main import residual


class ResidualTestCase(unittest.TestCase):
    def test_residual_greater_than_1(self):
        x1 = [2.5, 6.125, -9.0]
        x0 = [-2.0, 4.25, 1.7]

        self.assertEqual(2.3538802921168847, residual(x1, x0))


if __name__ == '__main__':
    unittest.main()
