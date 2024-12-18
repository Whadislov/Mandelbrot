"""Mandelbrot set
Set of complex numbers, c, for which an infinite sequence of numbers, z0, z1, .., zn, remains bounded
Recursive formula
zn+1 = zn**2 + c, z0 = 0
"""


import numpy as np
import warnings
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageEnhance
from dataclasses import dataclass
from mandelbrot import MandelbrotSet
from viewport import Viewport

warnings.filterwarnings("ignore")

'''
def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j #builds the matrix

def is_stable(c, num_iterations):
    z = 0
    for _ in range(num_iterations):
        z = z ** 2 + c #equation gets executed for each element of z as c is a scalar, thanks to Numpy's vectorization
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
'''

'''
mandelbrot_set = MandelbrotSet(max_iterations=256, escape_radius=1000)

width, height = 540, 350
scale = 0.00075
BLACK_AND_WHITE = "1"
GREY = "L" #luminance (range from 0 to 255)
'''
'''
image = Image.new(mode=BLACK_AND_WHITE, size=(width, height))
for y in range(height):
    for x in range(width):
        c = scale * complex(x - width / 2, height / 2 - y)
        image.putpixel((x, y), c not in mandelbrot_set) #white = c not in the set. putpixel expects a numerical value, bools in python are a subclass of integer

image = Image.new(mode=GREY, size=(width, height))
for y in range(height):
    for x in range(width):
        c = scale * complex(x - width / 2, height / 2 - y)
        instability = 1 - mandelbrot_set.stability(c, smooth=True) #stable = black, instable = white
        image.putpixel((x, y), int(instability * 255))
image.show()
'''


'''
for pixel in Viewport(image, center=-0.7435 + 0.1314j, width=0.002):
    c = complex(pixel)
    instability = 1 - mandelbrot_set.stability(c, smooth=True)
    pixel.color = int(instability * 255)
'''

mandelbrot_set = MandelbrotSet(max_iterations=512, escape_radius=1000)

#Helper function
def paint(mandelbrot_set, viewport, palette, smooth):
    for pixel in viewport:
        stability = mandelbrot_set.stability(complex(pixel), smooth)
        index = int(min(stability * len(palette), len(palette) - 1))
        pixel.color = palette[index % len(palette)]

#converts a normalized tuple (0.2, 0.11, 0.2) to (51, 28, 51), as Pillow values must range between 0 and 255
def denormalize(palette):
    return [
        tuple(int(channel * 255) for channel in color)
        for color in palette
    ]

#Get a colormap from matplotlib (normalized)
import matplotlib.cm
colormap = matplotlib.cm.get_cmap("twilight").colors
palette = denormalize(colormap)

image = Image.new(mode="RGB", size=(512, 512))
viewport = Viewport(image, center=-0.7435 + 0.1314j, width=0.002)
paint(mandelbrot_set, viewport, palette, smooth=True)
image.show()






