import numpy as np
from numpy import cos, power, sin, add, subtract
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
    # X(k + 1)
    x1 = list()
    # X(k)
    x0 = seed if (seed is not None) else initial_seed(n)
    if w == -1:
        w = best_w_value(n)
    delta_x = []
    k = 1
    r = r_tol
    max_z = power(n - 1, 2)
    while r >= r_tol:
        for z in range(1, max_z + 1):  # internal nodes
            new_z_node_value = sor(z, n, x1, x0, w, boundaries)
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


def residual(x1: list[float], x0: list[float]) -> float:
    arr1 = np.array(x1)
    arr0 = np.array(x0)
    return norm(add(arr1, arr0), 2) / norm(arr0, 2)


# cota
def error_bound(x1: list[float], x0: list[float]) -> float:
    arr1 = np.array(x1)
    arr0 = np.array(x0)
    return np.abs(subtract(arr1, arr0))


# frontera
def boundary_values_sum(
        z: int,
        n: int,
        boundaries: list[float]
) -> float:
    i, j = matrix_index_from(z, n)
    return b_value_from_matrix_index(i, j, n, boundaries)


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


# adjacents
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
    i = z // (n - 1)       # esta muy probablemente no va
    j = (z % (n - 1)) - 1  # formula:  j = z - (n - 1) * i - 1
    return j, i


def z_index_from(i: int, j: int, n: int) -> int:
    return (n - 1) * j + i + 1


def spectral_radius_gs(n: int) -> float:
    return power(cos(PI / n), 2)


def spectral_radius_sor(n: int) -> float:
    return best_w_value(n) - 1


def best_w_value(n: int) -> float:
    return 2 / (1 + sin(PI / n))
