import unittest
from main import z_index_from


class ZIndexFromTestCase(unittest.TestCase):

    def test_n_equal_to_4(self):
        n = 4

        self.assertEqual(1, z_index_from(0, 0, n))
        self.assertEqual(2, z_index_from(1, 0, n))
        self.assertEqual(3, z_index_from(2, 0, n))

        self.assertEqual(4, z_index_from(0, 1, n))
        self.assertEqual(5, z_index_from(1, 1, n))
        self.assertEqual(6, z_index_from(2, 1, n))

        self.assertEqual(7, z_index_from(0, 2, n))
        self.assertEqual(8, z_index_from(1, 2, n))
        self.assertEqual(9, z_index_from(2, 2, n))

    def test_n_equal_to_3(self):
        n = 3

        self.assertEqual(1, z_index_from(0, 0, n))
        self.assertEqual(2, z_index_from(1, 0, n))

        self.assertEqual(3, z_index_from(0, 1, n))
        self.assertEqual(4, z_index_from(1, 1, n))

    def test_n_equal_to_2(self):
        n = 2

        self.assertEqual(1, z_index_from(0, 0, n))


if __name__ == '__main__':
    unittest.main()
