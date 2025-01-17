import numpy as np

# Generate the coordinates with step size 0.1 in both x and y directions
x = np.arange(-4.0, 4.1, 0.1)
y = np.arange(-4.0, 4.1, 0.1)
z = 1.0  # Constant z value

# Create the grid
grid = [(round(i, 1), round(j, 1), z) for i in x for j in y]

# Format the grid into a readable string
formatted_output = "\n".join([f"({i:.1f} {j:.1f} {k:.1f})" for i, j, k in grid])

# Save the result to a file for easier access
output_path = "probe_grid.txt"
with open(output_path, "w") as file:
    file.write(formatted_output)

output_path
