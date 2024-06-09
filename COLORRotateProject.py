import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math

def colorId(pt):
    return ([(pt[0]+1)/2,(pt[1]+1)/2,(pt[2]+1)/2])
def colorInverse(pt):
    return ([1-(pt[0]+1)/2,1-(pt[1]+1)/2,1-(pt[2]+1)/2])
def colorFlop(pt,swap1,swap2,composite=False):
    pt[swap1],pt[swap2] = pt[swap2],pt[swap1]
    if(composite): return pt;
    else: return colorId(pt);
def newCords(pt):
    a = 1/math.sqrt(3)
    b = 1/math.sqrt(2)
    c = 1/(2*math.sqrt(2))
    d = 1/(math.sqrt(2))
    A = [[a,a,a],[b,-b,0],[-c,-c,d]]
    A = [
            [-c,-c,d],
            [b,-b,0],
            [a,a,a]
        ]

    pt = np.matmul(A,pt)
    return pt[0],pt[1],pt[2]

def projectRGB(u,v):
    pt = [(u+1)/2,(v+1)/2,(2-u)/2]
    return [max((u+1)/2,1),max((v+1)/2,1),max((2-u)/2,1)]

density = 0.05
x_range = np.arange(-10, 10, density)
y_range = np.arange(-10, 10, density)

x_coords = []
y_coords = []
z_coords = []
colorcoords = []

for i in x_range:
    for j in y_range:
        x_coords.append(i)
        y_coords.append(j)
        z_coords.append(0)
        colorcoords.append(projectRGB(i,j))

print(colorcoords)        

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_coords, y_coords, z_coords, c=colorcoords)

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-1, 2)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

print("(-1,-1,-1)=>",newCords([-1,-1,-1]))
print("(1,1,1)=>",newCords([1,1,1]))

plt.show()

