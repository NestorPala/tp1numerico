from main import matrix_index_from


def to_node_matrix(x: list[float], n: int) -> list[list[float]]:
    node_matrix = initialize_matrix_with_size(n - 1)

    for z in range(1, len(x) + 1):
        i, j = matrix_index_from(z, n)
        z_node_value = x[z - 1]
        node_matrix[i][j] = z_node_value

    return node_matrix


def initialize_matrix_with_size(size: int) -> list[list[float]]:
    matrix = []
    for i in range(size):
        matrix.append([])
    for i in range(size):
        for j in range(size):
            matrix[i].append(0)
    return matrix


# Unit tests
assert to_node_matrix([1, 2, 3, 4, 5, 6, 7, 8, 9], n=4) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
assert to_node_matrix([1, 2, 3, 4], n=3) == [[1, 3], [2, 4]]
assert to_node_matrix([1], n=2) == [[1]]
