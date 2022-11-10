import numpy as np
import matplotlib.pyplot as plt
import math
import numpy.polynomial.polynomial as poly


def get_y(x: float, z: float): 
    a = 9/4
    b = x*x + z*z - 1
    c = -9/80*z*z*z
    d = -x*x*z*z*z

    _a = a*a*a
    _b = 3*a*a*b
    _c = 3*a*b*b + c
    _d = b*b*b + d

    roots = np.real_if_close(np.roots([_a, _b, _c, _d]))
    roots = [x for x in roots if isinstance(x, float)]
    # print(roots, type(roots[0]))
    return roots

    

X, Y, Z = [], [], []
step = 0.5
for x in np.arange(-2.0, 2.0, step):
    for z in np.arange(-2.0, 2.0, step):
        y_list = get_y(x, z)
        for y in y_list:
            X.append(x)
            Y.append(y)
            Z.append(z)

# fig = plt.figure(dpi=120)
# ax = plt.axes(projection='3d')
# ax.scatter3D(X, Y, Z, c=Z, cmap='Greens');
# ax.set_xlabel('x')
# ax.set_xlim(-1.5, 1.5)
# ax.set_ylim(-1.5, 1.5)
# ax.set_zlim(-1.5, 1.5)
# ax.set_ylabel('y')
# ax.set_zlabel('z');

# plt.show()

# for angle in range(0, 360):
#     ax.view_init(90, angle)
#     plt.draw()
#     plt.pause(.001)