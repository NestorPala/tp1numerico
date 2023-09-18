# boundaries: [UPPER, LOWER, LEFT, RIGHT]
def solve_discrete_laplace_sor(
        n: int,
        r_tol: float,
        boundaries: list[int],
        w: float = -1,
        seed: list[float] = None
) -> set[list[float], list[float], float, int]:
    pass


def spectral_radius_gs(n: int) -> float:
    pass


def spectral_radius_sor(n: int) -> float:
    pass


def best_w_value(n: int) -> float:
    pass


def residual(x1: list[float], x0: list[float]) -> float:
    pass


def _2_norm(x: list[float]) -> float:
    pass


# calcular_valor_frontera
def b_value_from_matrix_index(
        i: int,
        j: int,
        n: int,
        boundaries: list[int]
) -> float:
    pass


# frontera
def boundary_values_sum(z: int) -> float:
    pass


def matrix_index_from(z: int, n: int) -> tuple[int, int]:
    pass


# no_frontera
def internal_values_sum(
        z: int,
        n: int,
        x1: list[float],
        x0: list[float]
) -> float:
    pass


# cota
def error_bound(x1: list[float], x0: list[float]) -> float:
    pass


def sor(
        z: int,
        n: int,
        x1: list[float],
        x0: list[float],
        w: float
) -> float:
    pass


def adjacents(z: int, n: int) -> list[int]:
    pass


def z_index_from(i: int, j: int) -> int:
    pass
