import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def colorId(pt):
    return ([(pt[0]+1)/2,(pt[1]+1)/2,(pt[2]+1)/2])
def colorInverse(pt):
    return ([1-(pt[0]+1)/2,1-(pt[1]+1)/2,1-(pt[2]+1)/2])
def colorFlop(pt,swap1,swap2):
    pt[swap1],pt[swap2] = pt[swap2],pt[swap1]
    return colorId(pt);


density = 0.2
# Define the range of coordinates
x_range = np.arange(-1, 1, density)
y_range = np.arange(-1, 1, density)
z_range = np.arange(-1, 1, density)

# Create lists to store coordinates
x_coords = []
y_coords = []
z_coords = []
colorcoords = []

# Generate all the points
for x in x_range:
    for y in y_range:
        for z in z_range:
            x_coords.append(x)
            y_coords.append(y)
            z_coords.append(z)
            #colorcoords.append(colorId(x,y,z))
            #colorcoords.append(colorInverse(x,y,z))
            colorcoords.append(colorFlop([x,y,z],0,1))

# Plot all the points
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_coords, y_coords, z_coords, c=colorcoords)

# Set axis limits
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

