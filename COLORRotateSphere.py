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
    A = [
            [-c,-c,d],
            [b,-b,0],
            [a,a,a]
        ]

    pt = np.matmul(A,pt)
    return pt[0],pt[1],pt[2]

def sphereProj(pt):
    return (pt[0]/(1-pt[2]),pt[1]/(1-pt[2]))

density = 0.05
x_range = np.arange(-1, 1, density)
y_range = np.arange(-1, 1, density)

x_coords = []
y_coords = []
z_coords = []
colorcoords = []

ze = np.array([0,0,0.999])
print(ze,"=>",sphereProj(ze))
print(-ze,"=>",sphereProj(-ze))

for side in range(6):
    for i in x_range:
        for j in y_range:
            x=0
            y=0
            z=0
            val = -1 if side < 3 else 1
            if(side%3==0):
                x = val; y=i;z=j;
            elif(side%3==1):
                x = i; y=val;z=j;
            elif(side%3==2):
                x = i; y=j;z=val;

            nx,ny,nz = newCords([x,y,z]); 
            mag = math.sqrt(nx*nx + ny*ny + nz*nz)
            '''
            x_coords.append(nx/mag)
            y_coords.append(ny/mag)
            z_coords.append(nz/mag)

            colorcoords.append(colorId([x,y,z]))
            #colorcoords.append(colorInverse([x,y,z]))
            #colorcoords.append(colorFlop([x,y,z],0,1))
            #colorcoords.append(colorFlop(colorFlop([x,y,z],0,1,True),1,2))
            '''

            proj = sphereProj([nx/mag,ny/mag,nz/mag])
            x_coords.append(proj[0])
            y_coords.append(proj[1])
            z_coords.append(0)
            colorcoords.append(colorInverse([x,y,z]))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_coords, y_coords, z_coords, c=colorcoords)

ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-2, 2)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_box_aspect([1,1,1])

print("(-1,-1,-1)=>",newCords([-1,-1,-1]))
print("(1,1,1)=>",newCords([1,1,1]))

plt.show()

