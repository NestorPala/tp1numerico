from main import boundary_values_sum, internal_values_sum
from math import isclose


# Machine epsilon for 1-decimal-digit round
U = 0.5e-01


# Check if result of all nodes are correct
# (approximately close each node to the sum of its adjacents)
def nodes_are_valid(
        x_values: list[float],
        x_errors: list[float],
        n: int,
        boundaries: list[float]
) -> bool:
    for z in range(1, len(x_values) + 1):
        b = boundary_values_sum(z, n, boundaries)
        i = internal_values_sum(z, n, x1=x_values, x0=x_values)
        adjacents_avg_value = (b + i) / 4
        z_node_value = x_values[z - 1]
        z_node_error = x_errors[z - 1]
        if not isclose(
                round(adjacents_avg_value, 1),
                round(z_node_value, 1),
                abs_tol=4 * (round(z_node_error, 1) + U)
        ):
            return False
    return True


assert nodes_are_valid(x_values=[10], x_errors=[0.0], n=2, boundaries=[10, 10, 10, 10])
assert nodes_are_valid(x_values=[25, 22.5, 27.5, 25], x_errors=[0.0, 0.0, 0.0, 0.0], n=3, boundaries=[10, 20, 30, 40])
