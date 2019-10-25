from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()

YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

x = 0
y = 0

def flatten(matrix):
    flattened = [pixel for row in matrix for pixel in row]
    return flattened

def gen_pipes(matrix):
    for row in matrix:
        row[-1] = RED
    gap = randint(1,6)
    matrix[gap][-1] = BLUE
    matrix[gap+1][+1] = BLUE
    matrix[gap-1][-1] = BLUE
    
    return matrix

def move_pipes(matrix):
    for row in matrix:
        for i in range(7):
            row[i] = row[i+1]
        row[-1] = BLUE
    return matrix

def draw_astronaut(event):
    global x
    global y
    
    sense.set_pixel(x,y,BLUE)
    
    if event.action == "pressed":
        if event.direction == "up":
            y = y-1
        elif event.direction == "down":
            y = y+1
        elif event.direction == "right":
            x+=1
        elif event.direction == "left":
            x-=1
    
    sense.set_pixel(x,y,YELLOW)
    




matrix = [[BLUE for column in range(8)] for row in range(8)]

sense.stick.direction_any = draw_astronaut

while True:
    matrix = gen_pipes(matrix)
    for i in range(4):
        sense.set_pixels(flatten(matrix))
        matrix = move_pipes(matrix)
        sleep(1)
