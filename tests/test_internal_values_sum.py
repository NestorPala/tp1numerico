import unittest
from main import internal_values_sum


class InternalValuesSumTestCase(unittest.TestCase):
    def test_n_equal_to_4_and_z_equal_to_1(self):
        z = 1
        n = 4
        x1 = []
        x0 = [9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0]
        self.assertEqual(14.0, internal_values_sum(z, n, x1, x0))

    def test_n_equal_to_4_and_z_in_middle(self):
        z = 6
        n = 4
        x1 = [8.5, 7.5, 6.5, 5.5, 4.5]
        x0 = [9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0]
        self.assertEqual(12.0, internal_values_sum(z, n, x1, x0))

    def test_n_equal_to_4_and_z_equal_to_last(self):
        z = 9
        n = 4
        x1 = [8.5, 7.5, 6.5, 5.5, 4.5, 3.5, 2.5, 1.5]
        x0 = [9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0]
        self.assertEqual(5.0, internal_values_sum(z, n, x1, x0))

    def test_n_equal_to_3_and_z_equal_to_1(self):
        z = 1
        n = 3
        x1 = []
        x0 = [4.0, 3.0, 2.0, 1.0]
        self.assertEqual(5.0, internal_values_sum(z, n, x1, x0))

    def test_n_equal_to_3_and_z_equal_to_2(self):
        z = 2
        n = 3
        x1 = [3.5]
        x0 = [4.0, 3.0, 2.0, 1.0]
        self.assertEqual(4.5, internal_values_sum(z, n, x1, x0))

    def test_n_equal_to_3_and_z_equal_to_3(self):
        z = 3
        n = 3
        x1 = [3.5, 4.0]
        x0 = [4.0, 3.0, 2.0, 1.0]
        self.assertEqual(4.5, internal_values_sum(z, n, x1, x0))

    def test_n_equal_to_3_and_z_equal_to_4(self):
        z = 4
        n = 3
        x1 = [3.5, 4.0, 3.5]
        x0 = [4.0, 3.0, 2.0, 1.0]
        self.assertEqual(7.5, internal_values_sum(z, n, x1, x0))

    def test_n_equal_to_2(self):
        z = 1
        n = 2
        x1 = []
        x0 = [4.0]
        self.assertEqual(0.0, internal_values_sum(z, n, x1, x0))


if __name__ == '__main__':
    unittest.main()
