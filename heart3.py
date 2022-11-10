from manim import *
import numpy as np
# import matplotlib.pyplot as plt
import math
from tqdm import tqdm

np.random.seed(42)
cloud_density = 0.04 # smaller is more expensive
outer_density = 0.8 # [0, 1]
sparkling_rate = 0.9 # 1: remains, 0: nothing
colors  = ['#FF1493', '#FFB3DE', '#FFF']
color_index = 1
z_range = (-1, 1)
x_range = (-2, 2)

def get_z(x: float, y: float, factor: float=1): 
    k = factor*x*x+9/80*y*y
    
    a = 1
    b = -(k ** (1.0/3))
    c = (x*x + 9/4*y*y - 1)
    
    delta = b**2 - 4*a*c
    if delta < 0:
        return []
    elif delta == 0:
        return [-b/2.0/a]
    else:
        delta_root = math.sqrt(delta)
        return [(-b+delta_root)/2/a, (-b-delta_root)/2/a]

def get_cloud(factor: float=1):
    X, Y, Z = [], [], []
    step = cloud_density # like density
    outer = 0.3
    # expand = 1.0
    z_min, z_max = 10, -10
    x_min, x_max = 10, -10
    for x in np.arange(-2.0, 2.0, step):
        for y in np.arange(-2.0, 2.0, step):
            x += np.random.uniform(-step, step)
            y += np.random.uniform(-step, step)
            x_min = min(x_min, x)
            x_max = max(x_max, x)
            z_list = get_z(x, y, factor)
            for z in z_list:
                # z += np.random.uniform(-step, step)
                z_min = min(z_min, z)
                z_max = max(z_max, z)
                X.append(x)
                Y.append(y)
                Z.append(z)

                if np.random.uniform(0, 1) < outer_density:
                    X.append(x*np.random.uniform(1, 1+outer))
                    Y.append(y*np.random.uniform(1, 1+outer))
                    Z.append(z*np.random.uniform(1, 1+outer))
    
    return X, Y, Z

class Heart(ThreeDScene):

    def construct(self):
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)

        factors = np.concatenate([np.arange(1, 2, 0.1), np.arange(2, 1, -0.1)])
        for i, factor in enumerate(factors):
            X, Z, Y = get_cloud(factor)
            print('got cloud')
            cloud = []
            for i in tqdm(range(len(X))):
                cloud.append(Dot([X[i], Y[i], Z[i]], radius=DEFAULT_DOT_RADIUS/5, color=colors[color_index]))
            for dot in tqdm(cloud):
                if np.random.uniform(0, 1) < sparkling_rate:
                    self.add(dot)
            self.wait(0.15)
            self.clear()
