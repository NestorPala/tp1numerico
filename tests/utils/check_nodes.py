from main import boundary_values_sum, internal_values_sum


def nodes_are_valid(x: list[float], n: int, boundaries: list[float]) -> bool:
    for z in range(1, len(x) + 1):
        b = boundary_values_sum(z, n, boundaries)
        i = internal_values_sum(z, n, x1=x, x0=x)
        adjacent_sum = b + i
        z_node_value = x[z - 1]
        if adjacent_sum / 4 != z_node_value:
            return False
    return True


assert nodes_are_valid(x=[10], n=2, boundaries=[10, 10, 10, 10])
assert nodes_are_valid(x=[25, 22.5, 27.5, 25], n=3, boundaries=[10, 20, 30, 40])
