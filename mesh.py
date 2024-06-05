import numpy as np

# Define the step size
step = 0.1

# Generate the 1D arrays for x and y coordinates
x = np.arange(0, 1 + step, step)
y = np.arange(0, 1 + step, step)

# Create the meshgrid
X, Y = np.meshgrid(x, y)

# Combine X and Y to get the desired 2D array
coordinates = np.column_stack((X.ravel(), Y.ravel()))

print(coordinates)

