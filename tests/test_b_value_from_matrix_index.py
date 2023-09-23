import unittest
from main import b_value_from_matrix_index, UPPER, LOWER, LEFT, RIGHT


class BValueFromMatrixIndexTestCase(unittest.TestCase):

    def test_n_equal_to_4(self):
        n = 4
        boundaries = [-1, -1, -1, -1]
        boundaries[UPPER] = 118
        boundaries[LOWER] = 56.25
        boundaries[LEFT] = -37
        boundaries[RIGHT] = 1
        self.assertEqual(19.25, b_value_from_matrix_index(0, 0, n, boundaries))
        self.assertEqual(-37, b_value_from_matrix_index(1, 0, n, boundaries))
        self.assertEqual(81, b_value_from_matrix_index(2, 0, n, boundaries))

        self.assertEqual(56.25, b_value_from_matrix_index(0, 1, n, boundaries))
        self.assertEqual(0, b_value_from_matrix_index(1, 1, n, boundaries))
        self.assertEqual(118, b_value_from_matrix_index(2, 1, n, boundaries))

        self.assertEqual(57.25, b_value_from_matrix_index(0, 2, n, boundaries))
        self.assertEqual(1, b_value_from_matrix_index(1, 2, n, boundaries))
        self.assertEqual(119, b_value_from_matrix_index(2, 2, n, boundaries))

    def test_n_equal_to_3(self):
        n = 3
        boundaries = [-1, -1, -1, -1]
        boundaries[UPPER] = 118
        boundaries[LOWER] = 56.25
        boundaries[LEFT] = -37
        boundaries[RIGHT] = 1
        self.assertEqual(19.25, b_value_from_matrix_index(0, 0, n, boundaries))
        self.assertEqual(81, b_value_from_matrix_index(1, 0, n, boundaries))

        self.assertEqual(57.25, b_value_from_matrix_index(0, 1, n, boundaries))
        self.assertEqual(119, b_value_from_matrix_index(1, 1, n, boundaries))

    def test_n_equal_to_2(self):
        n = 2
        boundaries = [-1, -1, -1, -1]
        boundaries[UPPER] = 118
        boundaries[LOWER] = 56.25
        boundaries[LEFT] = -37
        boundaries[RIGHT] = 1
        self.assertEqual(138.25, b_value_from_matrix_index(0, 0, n, boundaries))


if __name__ == '__main__':
    unittest.main()
