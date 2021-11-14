import numpy as np
import matplotlib.pyplot as plt
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import


def lorenz(x, y, z, s=10, r=1, b=2.667):
    '''
    Given:
       x, y, z: a point of interest in three dimensional space
       s, r, b: parameters defining the lorenz attractor
    Returns:
       x_dot, y_dot, z_dot: values of the lorenz attractor's partial
           derivatives at the point x, y, z
    '''
    x_dot = s * (y - x)
    y_dot = r * x - y - x * z
    z_dot = x * y - b * z
    return x_dot, y_dot, z_dot


dt = 0.01
num_steps = 10000

# creating step size for 2D graphs
t = np.linspace(0, 1, num_steps+1)

# Need one more for the initial values
xs = np.empty(num_steps + 1)
ys = np.empty(num_steps + 1)
zs = np.empty(num_steps + 1)

# Set initial values in kilobytes
xs[0], ys[0], zs[0] = (11.8, 4.4, 2.4)

# Step through "time", calculating the partial derivatives at the current point
# and using them to estimate the next point
x_dot, y_dot, z_dot = [], [], []
for i in range(num_steps):
    x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)
def plot1():
    # Plot of 3d graph
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.plot(xs, ys, zs, lw=0.5)
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Attractor r=1")
    plt.show()

    #plotting the x,y,and z plots
    fig, axs = plt.subplots(1, 3)
    axs[0].plot(t, xs)
    axs[0].set_title("X Plot r=1")
    axs[1].plot(t, ys)
    axs[1].set_title("Y Plot r=1")
    axs[2].plot(t, zs)
    axs[2].set_title("Z Plot r=1")
    plt.show()