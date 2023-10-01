from numpy import cos, power, sin, subtract, array, pi, log, log10
from numpy.linalg import norm

from tests.results.test_solve_discrete_laplace_sor.PARTE_1_C import RESULTS_1C_FOR_W_VALUE
from tests.results.test_solve_discrete_laplace_sor.PARTE_1_D_.RES_1D_W_1_00 import TEST_N_32_W_1_00_ITERATIONS, \
    TEST_N_32_W_1_00_RESIDUAL
from tests.results.test_solve_discrete_laplace_sor.PARTE_1_D_.RES_1D_W_1_05 import TEST_N_32_W_1_05_ITERATIONS, \
    TEST_N_32_W_1_05_RESIDUAL
from tests.results.test_solve_discrete_laplace_sor.PARTE_1_D_.RES_1D_W_1_10 import TEST_N_32_W_1_10_ITERATIONS, \
    TEST_N_32_W_1_10_RESIDUAL
from tests.results.test_solve_discrete_laplace_sor.PARTE_1_D_.RES_1D_W_1_15 import TEST_N_32_W_1_15_ITERATIONS, \
    TEST_N_32_W_1_15_RESIDUAL
from tests.results.test_solve_discrete_laplace_sor.PARTE_1_D_.RES_1D_W_1_20 import TEST_N_32_W_1_20_ITERATIONS, \
    TEST_N_32_W_1_20_RESIDUAL
from tests.results.test_solve_discrete_laplace_sor.PARTE_1_D_.RES_1D_W_1_25 import TEST_N_32_W_1_25_ITERATIONS, \
    TEST_N_32_W_1_25_RESIDUAL
from tests.results.test_solve_discrete_laplace_sor.PARTE_1_D_.RES_1D_W_1_30 import TEST_N_32_W_1_30_ITERATIONS, \
    TEST_N_32_W_1_30_RESIDUAL
from tests.results.test_solve_discrete_laplace_sor.PARTE_1_D_.RES_1D_W_1_35 import TEST_N_32_W_1_35_ITERATIONS, \
    TEST_N_32_W_1_35_RESIDUAL
from tests.results.test_solve_discrete_laplace_sor.PARTE_1_D_.RES_1D_W_1_40 import TEST_N_32_W_1_40_ITERATIONS, \
    TEST_N_32_W_1_40_RESIDUAL
from tests.results.test_solve_discrete_laplace_sor.PARTE_1_D_.RES_1D_W_1_45 import TEST_N_32_W_1_45_ITERATIONS, \
    TEST_N_32_W_1_45_RESIDUAL
from tests.results.test_solve_discrete_laplace_sor.PARTE_1_D_.RES_1D_W_1_50 import TEST_N_32_W_1_50_ITERATIONS, \
    TEST_N_32_W_1_50_RESIDUAL
from tests.results.test_solve_discrete_laplace_sor.PARTE_1_D_.RES_1D_W_1_55 import TEST_N_32_W_1_55_ITERATIONS, \
    TEST_N_32_W_1_55_RESIDUAL
from tests.results.test_solve_discrete_laplace_sor.PARTE_1_D_.RES_1D_W_1_60 import TEST_N_32_W_1_60_ITERATIONS, \
    TEST_N_32_W_1_60_RESIDUAL
from tests.results.test_solve_discrete_laplace_sor.PARTE_1_D_.RES_1D_W_1_65 import TEST_N_32_W_1_65_ITERATIONS, \
    TEST_N_32_W_1_65_RESIDUAL
from tests.results.test_solve_discrete_laplace_sor.PARTE_1_D_.RES_1D_W_1_70 import TEST_N_32_W_1_70_ITERATIONS, \
    TEST_N_32_W_1_70_RESIDUAL
from tests.results.test_solve_discrete_laplace_sor.PARTE_1_D_.RES_1D_W_1_75 import TEST_N_32_W_1_75_ITERATIONS, \
    TEST_N_32_W_1_75_RESIDUAL
from tests.results.test_solve_discrete_laplace_sor.PARTE_1_D_.RES_1D_W_1_80 import TEST_N_32_W_1_80_ITERATIONS, \
    TEST_N_32_W_1_80_RESIDUAL
from tests.results.test_solve_discrete_laplace_sor.PARTE_1_D_.RES_1D_W_1_85 import TEST_N_32_W_1_85_ITERATIONS, \
    TEST_N_32_W_1_85_RESIDUAL
from tests.results.test_solve_discrete_laplace_sor.PARTE_1_D_.RES_1D_W_1_90 import TEST_N_32_W_1_90_ITERATIONS, \
    TEST_N_32_W_1_90_RESIDUAL
from tests.results.test_solve_discrete_laplace_sor.PARTE_1_D_.RES_1D_W_1_95 import TEST_N_32_W_1_95_ITERATIONS, \
    TEST_N_32_W_1_95_RESIDUAL

PI = pi

# Boundaries list
UPPER = 0  # TN
LOWER = 1  # TS
LEFT = 2  # TW
RIGHT = 3  # TE

# Results tuple
X_VALUE = 0
X_ERROR_BOUND = 1
RESIDUAL = 2
ITERATIONS = 3


# Punto de entrada de la aplicación
def solve_discrete_laplace_sor(
        n: int,
        r_tol: float,
        boundaries: list[int],  # Contorno: [UPPER, LOWER, LEFT, RIGHT]
        w: float = -1,
        seed: list[float] = None  # X(0)
) -> tuple[list[float], list[float], float, int]:
    # X(k + 1)
    x1 = list()
    # X(k)
    x0 = seed if (seed is not None) else initial_seed(n)
    if w == -1:
        w = best_w_value(n)
    delta_x = []
    k = 1  # iterations
    r = r_tol
    max_z = power(n - 1, 2)  # amount of internal nodes
    while r >= r_tol:
        for z in range(1, max_z + 1):  # internal nodes
            new_z_node_value = node_sor(z, n, x1, x0, w, boundaries)
            x1.append(new_z_node_value)
        r = residual(x1, x0)
        if r >= r_tol:
            k += 1
            x0 = x1.copy()
            x1 = []
        else:
            delta_x = error_bound(x1, x0)
    return x1, delta_x, r, k


def initial_seed(n: int) -> list[int]:
    return [0 for i in range(power(n - 1, 2))]


def node_sor(
        z: int,
        n: int,
        x1: list[float],
        x0: list[float],
        w: float,
        boundaries: list[float]
) -> float:
    b = boundary_values_sum(z, n, boundaries)  # Temperaturas de los puntos del contorno
    i = internal_values_sum(z, n, x1, x0)  # Temperaturas de los nodos internos
    adjacent_sum = b + i   # Suma de todas las temperaturas adyacentes
    z0_value = x0[z - 1]  # T(z, k)
    z1_value = (adjacent_sum / 4 - z0_value) * w + z0_value  # SOR
    return z1_value  # T(z, k+1)


def residual(x1: list[float], x0: list[float]) -> float:
    arr1 = array(x1)
    arr0 = array(x0)
    return norm(subtract(arr1, arr0), 2) / norm(arr1, 2)


def error_bound(x1: list[float], x0: list[float]) -> list[float]:
    arr1 = array(x1)
    arr0 = array(x0)
    return list(abs(subtract(arr1, arr0)))


def boundary_values_sum(
        z: int,
        n: int,
        boundaries: list[float]
) -> float:
    i, j = matrix_index_from(z, n)  # No generamos la matriz A, calculamos sus posiciones
    return b_value_from_matrix_index(i, j, n, boundaries)


def b_value_from_matrix_index(
        i: int,
        j: int,
        n: int,
        boundaries: list[float]
) -> float:
    TN = boundaries[UPPER]
    TS = boundaries[LOWER]
    TW = boundaries[LEFT]
    TE = boundaries[RIGHT]

    # only one node
    if n == 2:
        return TN + TS + TW + TE

    # node is corner
    elif (i == 0) and (j == 0):
        return TS + TW
    elif (i == 0) and (j == n - 2):
        return TS + TE
    elif (i == n - 2) and (j == 0):
        return TN + TW
    elif (i == n - 2) and (j == n - 2):
        return TN + TE

    # node is border
    elif (i == 0) and (1 <= j <= n - 3):
        return TS
    elif (i == n - 2) and (1 <= j <= n - 3):
        return TN
    elif (j == 0) and (1 <= i <= n - 3):
        return TW
    elif (j == n - 2) and (1 <= i <= n - 3):
        return TE

    # node is center
    return 0.0


def internal_values_sum(
        z: int,
        n: int,
        x1: list[float],
        x0: list[float]
) -> float:
    total = 0.0
    for adj in internal_adjacents(z, n):
        if adj < z:
            total += x1[adj - 1]  # current iteration
        else:
            total += x0[adj - 1]  # last iteration
    return total


def internal_adjacents(z: int, n: int) -> list[int]:
    adj = []
    i, j = matrix_index_from(z, n)

    if j - 1 >= 0:
        z_adj = z_index_from(i, j - 1, n)
        adj.append(z_adj)

    if i - 1 >= 0:
        z_adj = z_index_from(i - 1, j, n)
        adj.append(z_adj)

    if i + 1 <= n - 2:
        z_adj = z_index_from(i + 1, j, n)
        adj.append(z_adj)

    if j + 1 <= n - 2:
        z_adj = z_index_from(i, j + 1, n)
        adj.append(z_adj)

    return adj


def matrix_index_from(z: int, n: int) -> tuple[int, int]:
    i = (z - 1) // (n - 1)
    j = z - (n - 1) * i - 1
    return j, i


def z_index_from(i: int, j: int, n: int) -> int:
    return (n - 1) * j + i + 1


def best_w_value(n: int) -> float:
    return 2 / (1 + sin(PI / n))


def spectral_radius_gs(n: int) -> float:
    return power(cos(PI / n), 2)


def spectral_radius_gs_from_residual(r: float, k: int) -> float:
    return r ** (1 / k)


def spectral_radius_sor(n: int) -> float:
    return best_w_value(n) - 1


values = list(map(lambda key: [RESULTS_1C_FOR_W_VALUE[key]["residual"], RESULTS_1C_FOR_W_VALUE[key]["iterations"]], RESULTS_1C_FOR_W_VALUE))

specradius = list(map(lambda value: spectral_radius_gs_from_residual(r=value[0],k=value[1]), values))

for sr in specradius:
    print(sr)


# RESULTS_1D_FOR_W_VALUE = {
#     1.00: {
#         "residual": TEST_N_32_W_1_00_RESIDUAL,
#         "iterations": TEST_N_32_W_1_00_ITERATIONS
#     },
#     1.05: {
#         "residual": TEST_N_32_W_1_05_RESIDUAL,
#         "iterations": TEST_N_32_W_1_05_ITERATIONS
#     },
#     1.10: {
#         "residual": TEST_N_32_W_1_10_RESIDUAL,
#         "iterations": TEST_N_32_W_1_10_ITERATIONS
#     },
#     1.15: {
#         "residual": TEST_N_32_W_1_15_RESIDUAL,
#         "iterations": TEST_N_32_W_1_15_ITERATIONS
#     },
#     1.20: {
#         "residual": TEST_N_32_W_1_20_RESIDUAL,
#         "iterations": TEST_N_32_W_1_20_ITERATIONS
#     },
#     1.25: {
#         "residual": TEST_N_32_W_1_25_RESIDUAL,
#         "iterations": TEST_N_32_W_1_25_ITERATIONS
#     },
#     1.30: {
#         "residual": TEST_N_32_W_1_30_RESIDUAL,
#         "iterations": TEST_N_32_W_1_30_ITERATIONS
#     },
#     1.35: {
#         "residual": TEST_N_32_W_1_35_RESIDUAL,
#         "iterations": TEST_N_32_W_1_35_ITERATIONS
#     },
#     1.40: {
#         "residual": TEST_N_32_W_1_40_RESIDUAL,
#         "iterations": TEST_N_32_W_1_40_ITERATIONS
#     },
#     1.45: {
#         "residual": TEST_N_32_W_1_45_RESIDUAL,
#         "iterations": TEST_N_32_W_1_45_ITERATIONS
#     },
#     1.50: {
#         "residual": TEST_N_32_W_1_50_RESIDUAL,
#         "iterations": TEST_N_32_W_1_50_ITERATIONS
#     },
#     1.55: {
#         "residual": TEST_N_32_W_1_55_RESIDUAL,
#         "iterations": TEST_N_32_W_1_55_ITERATIONS
#     },
#     1.60: {
#         "residual": TEST_N_32_W_1_60_RESIDUAL,
#         "iterations": TEST_N_32_W_1_60_ITERATIONS
#     },
#     1.65: {
#         "residual": TEST_N_32_W_1_65_RESIDUAL,
#         "iterations": TEST_N_32_W_1_65_ITERATIONS
#     },
#     1.70: {
#         "residual": TEST_N_32_W_1_70_RESIDUAL,
#         "iterations": TEST_N_32_W_1_70_ITERATIONS
#     },
#     1.75: {
#         "residual": TEST_N_32_W_1_75_RESIDUAL,
#         "iterations": TEST_N_32_W_1_75_ITERATIONS
#     },
#     1.80: {
#         "residual": TEST_N_32_W_1_80_RESIDUAL,
#         "iterations": TEST_N_32_W_1_80_ITERATIONS
#     },
#     1.8214651907890225: {
#         "residual": 0.009862712316656284,
#         "iterations": 28
#     },
#     1.85: {
#         "residual": TEST_N_32_W_1_85_RESIDUAL,
#         "iterations": TEST_N_32_W_1_85_ITERATIONS
#     },
#     1.90: {
#         "residual": TEST_N_32_W_1_90_RESIDUAL,
#         "iterations": TEST_N_32_W_1_90_ITERATIONS
#     },
#     1.95: {
#         "residual": TEST_N_32_W_1_95_RESIDUAL,
#         "iterations": TEST_N_32_W_1_95_ITERATIONS
#     },
# }
#
# values = list(map(lambda key: [RESULTS_1D_FOR_W_VALUE[key]["residual"], RESULTS_1D_FOR_W_VALUE[key]["iterations"]], RESULTS_1D_FOR_W_VALUE))
#
# specradius = list(map(lambda value: spectral_radius_gs_from_residual(r=value[0],k=value[1]), values))
#
# for sr in specradius:
#     print(sr)
#     # print(str(round(sr, 3))[0:1] + "," + str(round(sr, 3))[2:5])


print(spectral_radius_sor(4))
#
# print(spectral_radius_sor(32))
