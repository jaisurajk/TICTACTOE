import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# def pyramid(n, height):
#     theta = np.linspace(0, 2*np.pi, n+1)
#     x = np.cos(theta)
#     y = np.sin(theta)
#     z = np.zeros(n+1)
#     x_coor = np.zeros_like(x)
#     y_coor = np.zeros_like(y)
#     z_coor = np.full(n+1, height)
#     X = np.vstack([x, x_coor])
#     Y = np.vstack([y, y_coor])
#     Z = np.vstack([z, z_coor])
#     return X, Y, Z

def pyramid(n, height):
    theta = np.linspace(0, 2*np.pi, n+1)[:-1]
    x = np.cos(theta)
    y = np.sin(theta)
    z = np.zeros(n)
    X, Y = np.meshgrid(x, y)
    Z = np.ones((n, n)) * height / n
    for i in range(n):
        for j in range(n-i):
            Z[i,j] += i * height / n
            Z[i,n-j-1] += i * height / n
    return X, Y, Z
# Generate the two pyramids
# x1, y1, z1 = pyramid(4, 5)
# x2, y2, z2 = pyramid(6, 10)

# # Create a 3D figure
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # Plot the first pyramid
# ax.plot_surface(x1, y1, z1, color='r')
# # Plot the second pyramid
# ax.plot_surface(x2, y2, z2, color='b')

# # Set the axis limits and labels
# ax.set_xlim(-1.5, 1.5)
# ax.set_ylim(-1.5, 1.5)
# ax.set_zlim(0, 12)
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')

# # Show the plot
# plt.show()

if __name__ == '__main__':
    
    fig = plt.figure(tight_layout=True)
    ax = plt.axes(projection = '3d')
    x, y, z = pyramid(4, 5)
    ax.contour3D (x, y, z, 50)
    ax = plt.axes(projection = '3d')
    x, y, z = pyramid(6, 10)
    ax.contour3D(x, y, z, 50)
    plt.show()