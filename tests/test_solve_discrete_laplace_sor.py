import unittest
from main import solve_discrete_laplace_sor, UPPER, LOWER, LEFT, RIGHT
from tests.results.test_solve_discrete_laplace_sor.PARTE_1_D_.RES_1D_W_1_446 import TEST_N_32_W_1_446_X_VALUE, TEST_N_32_W_1_446_X_ERROR_BOUND, TEST_N_32_W_1_446_RESIDUAL, TEST_N_32_W_1_446_ITERATIONS
from tests.results.test_solve_discrete_laplace_sor.PARTE_2 import TEST_1_X_VALUE, TEST_1_X_ERROR_BOUND, TEST_1_RESIDUAL, TEST_1_ITERATIONS

X_VALUE = 0
X_ERROR_BOUND = 1
RESIDUAL = 2
ITERATIONS = 3


class SolveDiscreteLaplaceSORTestCase(unittest.TestCase):

    # Parte 2
    # TODO: do for w values: [1.00, 1.05, 1.10, ..., 1.95]
    # Test 1
    def test_n_equals_8(self):
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

        x_value = data[X_VALUE]
        x_error_bound = data[X_ERROR_BOUND]
        residual = data[RESIDUAL]
        iterations = data[ITERATIONS]

        self.assertEqual(TEST_1_X_VALUE, x_value)
        self.assertEqual(TEST_1_X_ERROR_BOUND, x_error_bound)
        self.assertEqual(TEST_1_RESIDUAL, residual)
        self.assertEqual(TEST_1_ITERATIONS, iterations)

    # c) (N = 4), d)
    def test_n_equals_32(self):
        n = 32
        r_tol = 0.01
        boundaries = [-1, -1, -1, -1]

        # 108244
        boundaries[UPPER] = 1.0
        boundaries[LOWER] = 1.0
        boundaries[LEFT] = 1.0
        boundaries[RIGHT] = 1.0

        # w = 1.4464626921716894
        data = solve_discrete_laplace_sor(n, r_tol, boundaries)

        x_value = data[X_VALUE]
        x_error_bound = data[X_ERROR_BOUND]
        residual = data[RESIDUAL]
        iterations = data[ITERATIONS]

        print(x_value)
        print(x_error_bound)

        self.assertEqual(TEST_N_32_W_1_446_X_VALUE, x_value)
        self.assertEqual(TEST_N_32_W_1_446_X_ERROR_BOUND, x_error_bound)
        self.assertEqual(TEST_N_32_W_1_446_RESIDUAL, residual)
        self.assertEqual(TEST_N_32_W_1_446_ITERATIONS, iterations)


if __name__ == '__main__':
    unittest.main()
