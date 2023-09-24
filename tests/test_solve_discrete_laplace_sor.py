import unittest
from unittest import skip

from main import solve_discrete_laplace_sor, UPPER, LOWER, LEFT, RIGHT
from tests.results.test_solve_discrete_laplace_sor.PARTE_1_D_.RES_1D_W_1_446 import \
    TEST_N_32_W_1_446_X_VALUE, \
    TEST_N_32_W_1_446_X_ERROR_BOUND, \
    TEST_N_32_W_1_446_RESIDUAL, \
    TEST_N_32_W_1_446_ITERATIONS
from tests.results.test_solve_discrete_laplace_sor.PARTE_2 import \
    TEST_1_X_VALUE, \
    TEST_1_X_ERROR_BOUND, \
    TEST_1_RESIDUAL, \
    TEST_1_ITERATIONS
from tests.utils.check_nodes import nodes_are_valid


X_VALUE = 0
X_ERROR_BOUND = 1
RESIDUAL = 2
ITERATIONS = 3


class SolveDiscreteLaplaceSORTestCase(unittest.TestCase):

    # Parte 2
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

        # w = best_w_value(n)
        data = solve_discrete_laplace_sor(n, r_tol, boundaries)

        x_values = data[X_VALUE]
        x_errors = data[X_ERROR_BOUND]
        residual = data[RESIDUAL]
        iterations = data[ITERATIONS]

        self.assertEqual(TEST_1_X_VALUE, x_values)
        self.assertEqual(TEST_1_X_ERROR_BOUND, x_errors)
        self.assertEqual(TEST_1_RESIDUAL, residual)
        self.assertEqual(TEST_1_ITERATIONS, iterations)

        self.assertTrue(nodes_are_valid(x_values, x_errors, n, boundaries))

    # c) (N = 4), d)
    def test_n_equals_32(self):
        n = 32
        r_tol = 0.01
        boundaries = [-1, -1, -1, -1]

        boundaries[UPPER] = 1.0
        boundaries[LOWER] = 1.0
        boundaries[LEFT] = 1.0
        boundaries[RIGHT] = 1.0

        # w = best_w_value(n)
        data = solve_discrete_laplace_sor(n, r_tol, boundaries)

        x_values = data[X_VALUE]
        x_errors = data[X_ERROR_BOUND]
        residual = data[RESIDUAL]
        iterations = data[ITERATIONS]

        self.assertEqual(TEST_N_32_W_1_446_X_VALUE, x_values)
        self.assertEqual(TEST_N_32_W_1_446_X_ERROR_BOUND, x_errors)
        self.assertEqual(TEST_N_32_W_1_446_RESIDUAL, residual)
        self.assertEqual(TEST_N_32_W_1_446_ITERATIONS, iterations)

        self.assertTrue(nodes_are_valid(x_values, x_errors, n, boundaries))

    def test_n_equals_128(self):
        n = 128
        r_tol = 0.01
        boundaries = [-1, -1, -1, -1]

        boundaries[UPPER] = 1.0
        boundaries[LOWER] = 1.0
        boundaries[LEFT] = 1.0
        boundaries[RIGHT] = 1.0

        data = solve_discrete_laplace_sor(n, r_tol, boundaries)

        x_values = data[X_VALUE]
        x_errors = data[X_ERROR_BOUND]

        self.assertTrue(nodes_are_valid(x_values, x_errors, n, boundaries))

    @skip('(n = 256) Takes too long')
    def test_n_equals_256(self):
        n = 256
        r_tol = 0.01
        boundaries = [-1, -1, -1, -1]

        boundaries[UPPER] = 1.0
        boundaries[LOWER] = 1.0
        boundaries[LEFT] = 1.0
        boundaries[RIGHT] = 1.0

        data = solve_discrete_laplace_sor(n, r_tol, boundaries)

        x_values = data[X_VALUE]
        x_errors = data[X_ERROR_BOUND]

        self.assertTrue(nodes_are_valid(x_values, x_errors, n, boundaries))

    @skip('(n = 512) Takes too long')
    def test_n_equals_512(self):
        n = 512
        r_tol = 0.01
        boundaries = [-1, -1, -1, -1]

        boundaries[UPPER] = 1.0
        boundaries[LOWER] = 1.0
        boundaries[LEFT] = 1.0
        boundaries[RIGHT] = 1.0

        data = solve_discrete_laplace_sor(n, r_tol, boundaries)

        x_values = data[X_VALUE]
        x_errors = data[X_ERROR_BOUND]

        self.assertTrue(nodes_are_valid(x_values, x_errors, n, boundaries))

    @skip('(n = 1024) Takes too long')
    def test_n_equals_1024(self):
        n = 1024
        r_tol = 0.01
        boundaries = [-1, -1, -1, -1]

        boundaries[UPPER] = 1.0
        boundaries[LOWER] = 1.0
        boundaries[LEFT] = 1.0
        boundaries[RIGHT] = 1.0

        data = solve_discrete_laplace_sor(n, r_tol, boundaries)

        x_values = data[X_VALUE]
        x_errors = data[X_ERROR_BOUND]

        self.assertTrue(nodes_are_valid(x_values, x_errors, n, boundaries))


if __name__ == '__main__':
    unittest.main()
