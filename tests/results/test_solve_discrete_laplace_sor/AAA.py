from main import UPPER, LOWER, LEFT, RIGHT, solve_discrete_laplace_sor
from tests.test_solve_discrete_laplace_sor import X_VALUE, X_ERROR_BOUND, RESIDUAL, ITERATIONS


n = 4
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

print(x_value)
print(x_error_bound)
print(residual)
print(iterations)
