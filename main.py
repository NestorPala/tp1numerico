import numpy as np
from numpy import cos, power, sin, add, ndarray, subtract
from numpy.linalg import norm


PI = np.pi
UPPER = 0
LOWER = 1
LEFT = 2
RIGHT = 3


# boundaries: [UPPER, LOWER, LEFT, RIGHT]
def solve_discrete_laplace_sor(
        n: int,
        r_tol: float,
        boundaries: list[int],
        w: float = -1,
        seed: list[float] = None
) -> tuple[list[float], list[float], float, int]:
    x1 = list()
    x0 = seed if (seed is not None) else [0 for i in range(n)]
    k = 0
    r = r_tol
    delta_x = []
    max_z = power(n - 1, 2)
    while r >= r_tol:
        x1 = []
        for z in range(1, max_z + 1):
            tz1 = sor(z, n, x1, x0, w, boundaries)
            x1.append(tz1)
        delta_x = error_bound(x1, x0)
        r = residual(x1, x0)
        x0 = x1.copy()
    return x1, delta_x, r, k


def spectral_radius_gs(n: int) -> float:
    return power(cos(PI / n), 2)


def spectral_radius_sor(n: int) -> float:
    return best_w_value(n) - 1


def best_w_value(n: int) -> float:
    return 2 / (1 + sin(PI / n))


def residual(x1: list[float], x0: list[float]) -> float:
    arr1 = np.array(x1)
    arr0 = np.array(x0)
    return _2_norm(add(arr1, arr0)) / _2_norm(arr0)


def _2_norm(x: ndarray) -> float:
    return norm(x, 2)


# calcular_valor_frontera
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

    if (i == 0) and (j == 0):
        return TS + TW
    elif (i == n - 2) and (j == 0):
        return TN + TW
    elif (i == 0) and (j == n - 2):
        return TS + TE
    elif (i == n - 2) and (j == n - 2):
        return TN + TE
    elif (i == 0) and (1 <= j <= n - 3):
        return TS
    elif (1 <= i <= n - 3) and (j == 0):
        return TN
    elif (1 <= i <= n - 3) and (j == n - 2):
        return TW
    elif (1 <= i <= n - 3) and (1 <= j <= n - 3):
        return TE

    return 0.0


# frontera
def boundary_values_sum(
        z: int,
        n: int,
        boundaries: list[float]
) -> float:
    i, j = matrix_index_from(z, n)
    return b_value_from_matrix_index(i, j, n, boundaries)


def matrix_index_from(z: int, n: int) -> tuple[int, int]:
    i = z // (n - 1)
    j = (z % (n - 1)) - 1
    return j, i


# no_frontera
def internal_values_sum(
        z: int,
        n: int,
        x1: list[float],
        x0: list[float]
) -> float:
    total = 0.0
    for adj in internal_adjacents(z, n):
        if adj < z:
            total += x1[adj]  # current iteration
        else:
            total += x0[adj]  # last iteration
    return total


# cota
def error_bound(x1: list[float], x0: list[float]) -> float:
    arr1 = np.array(x1)
    arr0 = np.array(x0)
    return np.abs(subtract(arr1, arr0))


def sor(
        z: int,
        n: int,
        x1: list[float],
        x0: list[float],
        w: float,
        boundaries: list[float]
) -> float:
    b = boundary_values_sum(z, n, boundaries)
    i = internal_values_sum(z, n, x1, x0)
    adjacent_sum = b + i
    z0_value = x0[z - 1]
    z1_value = (adjacent_sum / 4 - z0_value) * w + z0_value
    return z1_value


# adjacents
def internal_adjacents(z: int, n: int) -> list[int]:
    adj = []
    i, j = matrix_index_from(z, n)

    if j-1 >= 0:
        z_adj = z_index_from(i, j-1, n)
        adj.append(z_adj)

    if i-1 >= 0:
        z_adj = z_index_from(i-1, j, n)
        adj.append(z_adj)

    if i+1 <= n-2:
        z_adj = z_index_from(i+1, j, n)
        adj.append(z_adj)

    if j+1 <= n-2:
        z_adj = z_index_from(i, j+1, n)
        adj.append(z_adj)

    return adj


def z_index_from(i: int, j: int, n: int) -> int:
    return (n - 1) * j + (i + 1)
