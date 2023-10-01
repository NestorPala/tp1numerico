import matplotlib.pyplot as plt
import numpy as np

from tests.results.test_solve_discrete_laplace_sor.PARTE_1_C import RESULTS_1C_FOR_W_VALUE
from tests.results.test_solve_discrete_laplace_sor.PARTE_1_D_.RES_1D_W_1_80 import TEST_N_32_W_1_80_X_VALUE
from tests.utils.to_node_matrix import to_node_matrix

n = 32
#array = to_node_matrix(RESULTS_1C_FOR_W_VALUE[1.00]["x_value"], n=n)

array = to_node_matrix(TEST_N_32_W_1_80_X_VALUE, n)

# Define your matrix of floats (replace this with your data)
matrix = np.array(array)

# Create a colormap for coloring the sections
cmap = plt.get_cmap('viridis')

# Create a figure and axis
fig, ax = plt.subplots()

# Loop through the matrix to create and color the squares
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        color = cmap(matrix[i, j])  # Color based on the matrix value
        ax.add_patch(plt.Rectangle((j, i), 1, 1, color=color))

# Set axis limits and labels
ax.set_xlim(0, matrix.shape[1])
ax.set_ylim(0, matrix.shape[0])
ax.set_xticks(np.arange(matrix.shape[1]))
ax.set_yticks(np.arange(matrix.shape[0]))
ax.set_xticklabels([str(i) for i in range(matrix.shape[1])])
ax.set_yticklabels([str(i) for i in range(matrix.shape[0])])
ax.set_xlabel('Column')
ax.set_ylabel('Row')

# Add a colorbar to show the mapping of values to colors
cbar = plt.colorbar(plt.cm.ScalarMappable(norm=None, cmap=cmap), ax=ax)
cbar.set_label('Matrix Values')

# Display the plot
plt.title('Squared Regions Colored by Sections')
plt.grid(visible=True)
plt.show()