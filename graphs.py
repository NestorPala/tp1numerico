import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize

from tests.results.test_solve_discrete_laplace_sor.PARTE_2 import TEST_1_X_VALUE
from tests.utils.to_node_matrix import to_node_matrix

n = 8
array = to_node_matrix(TEST_1_X_VALUE, n)

# Define your matrix of floats (replace this with your data)
matrix = np.array(array)

# Define the desired minimum and maximum values for the color range
vmin = 20.0
vmax = 80.0

# Define the number of levels for color discretization
num_levels = 18  # You can adjust this number as needed

# Create a normalization object to control the color range
norm = Normalize(vmin=vmin, vmax=vmax)

# Create a colormap with the specified number of levels
cmap = plt.get_cmap('hot', num_levels)

# Create a figure and axis
fig, ax = plt.subplots()

# Loop through the matrix to create and color the squares
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        color = cmap(norm(matrix[i, j]))  # Color based on the matrix value and the normalization
        ax.add_patch(plt.Rectangle((j, i), 1, 1, color=color))

# Set axis limits and labels
ax.set_xlim(0, matrix.shape[1])
ax.set_ylim(0, matrix.shape[0])
ax.set_xticks(np.arange(matrix.shape[1]))
ax.set_yticks(np.arange(matrix.shape[0]))
ax.set_xticklabels([str(i) for i in range(matrix.shape[1])])
ax.set_yticklabels([str(i) for i in range(matrix.shape[0])])

# Add a colorbar to show the mapping of values to colors
cbar = plt.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax)
cbar.set_label('Temperature (°C)')

# Display the plot
plt.title('Internal points/nodes in a motherboard')
plt.grid(visible=True)
plt.show()
