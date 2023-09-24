from main import UPPER, LOWER, LEFT, RIGHT, solve_discrete_laplace_sor, best_w_value
from tests.test_solve_discrete_laplace_sor import X_VALUE, X_ERROR_BOUND, RESIDUAL, ITERATIONS


n = 32
r_tol = 0.01
boundaries = [-1, -1, -1, -1]
# 108244
boundaries[UPPER] = 1.0
boundaries[LOWER] = 1.0
boundaries[LEFT] = 1.0
boundaries[RIGHT] = 1.0
w = 1.95

data = solve_discrete_laplace_sor(n, r_tol, boundaries, w)

x_value = data[X_VALUE]
x_error_bound = data[X_ERROR_BOUND]
residual = data[RESIDUAL]
iterations = data[ITERATIONS]

w_str_decimals = '{:.2f}'.format(w)[2:4]
print(f"TEST_N_32_W_1_{w_str_decimals}_X_VALUE =", x_value, "\n")
print(f"TEST_N_32_W_1_{w_str_decimals}_X_ERROR_BOUND =", x_error_bound, "\n")
print(f"TEST_N_32_W_1_{w_str_decimals}_RESIDUAL =", residual, "\n")
print(f"TEST_N_32_W_1_{w_str_decimals}_ITERATIONS =", iterations, "\n")
