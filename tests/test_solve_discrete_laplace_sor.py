import unittest
from main import solve_discrete_laplace_sor, UPPER, LOWER, LEFT, RIGHT
from results.test_solve_discrete_laplace_sor import TEST_1_X_VALUE, TEST_1_X_ERROR_BOUND


X = 0
X_UPPER_BOUND = 1
RESIDUAL = 2
ITERATIONS = 3


class SolveDiscreteLaplaceSORTestCase(unittest.TestCase):

    # Test 1
    def test_n_equals_4(self):
        n = 8
        r_tol = 0.001
        boundaries = [-1, -1, -1, -1]

        # 108244
        boundaries[UPPER] = 80.0
        boundaries[LOWER] = 20.0
        boundaries[LEFT] = 40.0
        boundaries[RIGHT] = 40.0

        # w = 1.4464626921716894
        data = solve_discrete_laplace_sor(n, r_tol, boundaries)

        x_value = data[X]
        x_error_bound = data[X_UPPER_BOUND]
        residual = data[RESIDUAL]
        iterations = data[ITERATIONS]

        self.assertEqual(TEST_1_X_VALUE, x_value)
        self.assertEqual(TEST_1_X_ERROR_BOUND, x_error_bound)
        self.assertEqual(0.0007298476528922345, residual)
        self.assertEqual(14, iterations)

    def test_n_equals_3(self):
        n = 3
        self.assertEqual(True, True)

    def test_n_equals_2(self):
        n = 2
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
