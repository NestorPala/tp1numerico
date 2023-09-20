import unittest
from main import boundary_values_sum


class BoundaryValuesSumTestCase(unittest.TestCase):

    def test_n_equal_to_4(self):
        n = 4
        boundaries = [1, 1, 1, 1]
        self.assertEqual(2, boundary_values_sum(1, n, boundaries))
        self.assertEqual(1, boundary_values_sum(2, n, boundaries))
        self.assertEqual(2, boundary_values_sum(3, n, boundaries))
        self.assertEqual(1, boundary_values_sum(4, n, boundaries))
        self.assertEqual(0, boundary_values_sum(5, n, boundaries))
        self.assertEqual(1, boundary_values_sum(6, n, boundaries))
        self.assertEqual(2, boundary_values_sum(7, n, boundaries))
        self.assertEqual(1, boundary_values_sum(8, n, boundaries))
        self.assertEqual(2, boundary_values_sum(9, n, boundaries))

    def test_n_equal_to_3(self):
        n = 3
        boundaries = [1, 1, 1, 1]
        self.assertEqual(2, boundary_values_sum(1, n, boundaries))
        self.assertEqual(2, boundary_values_sum(2, n, boundaries))
        self.assertEqual(2, boundary_values_sum(3, n, boundaries))
        self.assertEqual(2, boundary_values_sum(4, n, boundaries))

    def test_n_equal_to_2(self):
        n = 2
        boundaries = [1, 1, 1, 1]
        self.assertEqual(4, boundary_values_sum(1, n, boundaries))


if __name__ == '__main__':
    unittest.main()
