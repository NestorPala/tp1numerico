import unittest
from main import residual


class ResidualTestCase(unittest.TestCase):
    def test_residual_greater_than_1(self):
        x1 = [2.5, 6.125, -9.0]
        x0 = [-2.0, 4.25, 1.7]

        self.assertEqual(1.0526740854219663, residual(x1, x0))


if __name__ == '__main__':
    unittest.main()
