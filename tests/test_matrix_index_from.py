import unittest
from main import matrix_index_from


class MatrixIndexFromTestCase(unittest.TestCase):

    def test_n_equal_to_4(self):
        n = 4

        self.assertEqual((0, 0), matrix_index_from(1, n))
        self.assertEqual((1, 0), matrix_index_from(2, n))
        # self.assertEqual((2, 0), matrix_index_from(3, n))
        #
        self.assertEqual((0, 1), matrix_index_from(4, n))
        self.assertEqual((1, 1), matrix_index_from(5, n))
        # self.assertEqual((2, 1), matrix_index_from(6, n))
        #
        self.assertEqual((0, 2), matrix_index_from(7, n))
        self.assertEqual((1, 2), matrix_index_from(8, n))
        # self.assertEqual((2, 2), matrix_index_from(9, n))

    def test_n_equal_to_3(self):
        n = 3

        # self.assertEqual((0, 0), matrix_index_from(1, n))
        # self.assertEqual((1, 0), matrix_index_from(2, n))

        self.assertEqual((0, 1), matrix_index_from(3, n))
        # self.assertEqual((1, 1), matrix_index_from(4, n))

    # def test_n_equal_to_2(self):
    #     n = 2
    #
    #     self.assertEqual((0, 0), matrix_index_from(1, n))


if __name__ == '__main__':
    unittest.main()
