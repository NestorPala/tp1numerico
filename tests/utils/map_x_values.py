from math import ceil


def round_x_values(x_values: list[float], digits: int = 2) -> list[float]:
    return list(
        map(lambda value: round(value, digits), x_values)
    )


def ceiling_x_values(
        x_values: list[float],
        significant_digits: int = 1
) -> list[float]:
    def round_up(x: float) -> float:
        return ceil(x * 10 ** significant_digits) / 10 ** significant_digits

    return list(
        map(lambda value: round_up(value), x_values)
    )
