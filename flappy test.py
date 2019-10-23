from sense_hat import SenseHat
from random import randint

sense = SenseHat()

def flatten(matrix):
    flattened = [pixel for row in matrix for pixel in row]
    return flattened

#g = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

"""creeper_pixels = [
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, b, b, g, g, b, b, g,
    g, b, b, g, g, b, b, g,
    g, g, g, b, b, g, g, g,
    g, g, b, b, b, b, g, g,
    g, g, b, b, b, b, g, g,
    g, g, b, g, g, b, g, g
]"""

#sense.set_pixels(creeper_pixels)

matrix = [[BLUE for column in range(8)] for row in range(8)]
gap = randint(1,6)
for row in matrix:
    row[-1] = RED

print (matrix)
matrix = flatten(matrix)
sense.set_pixels(matrix)