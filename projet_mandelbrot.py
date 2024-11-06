"""Mandelbrot set
Set of complex numbers, c, for which an infinite sequence of numbers, z0, z1, .., zn, remains bounded
Recursive formula
zn+1 = zn**2 + c, z0 = 0
"""

import numpy as np
import warnings
import matplotlib.pyplot as plt
from PIL import Image

warnings.filterwarnings("ignore")

def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    print(re)
    im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j #builds the matrix

def is_stable(c, num_iterations):
    z = 0
    for _ in range(num_iterations):
        z = z ** 2 + c #equation gets executed for each element of z as c is a scalar thanks to Numpy's vectorization
    return abs(z) < 2 #mask (= boolean matrix of the size of z)

def get_members(c, num_iterations):
    mask = is_stable(c, num_iterations)
    return c[mask] #returns the candidates that are stable


c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=1024)

#draw with matplotlib

plt.imshow(is_stable(c, num_iterations=20), cmap="binary_r")
plt.gca().set_aspect("equal")
plt.axis("off")
plt.tight_layout()
plt.show()

#draw with pillow
image = Image.effect_mandelbrot((2048, 2048), (-3, -2.5, 2, 2.5), 100).show()
image.show()
