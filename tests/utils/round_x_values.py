def round_x_values(x: list[float], digits: int = 2) -> list[float]:
    return list(
        map(lambda value: round(value, digits), x)
    )
