from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()
game_over = False
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
    global game_over    
    sense.set_pixel(x,y,BLUE)    
    if event.action == "pressed":
        if event.direction == "up" and y>0:
            y-=1
        elif event.direction == "down" and y<7:
            y+=1
        elif event.direction == "right" and x<7:
            x+=1
        elif event.direction == "left" and x>0:
            x-=1
    sense.set_pixel(x,y,YELLOW)
    if matrix[y][x] == RED:
        game_over = True
    
def check_collision(matrix):
    if matrix[y][x] == RED:
        return True
    else:
        return False


matrix = [[BLUE for column in range(8)] for row in range(8)]

sense.stick.direction_any = draw_astronaut

while not game_over:
    matrix = gen_pipes(matrix)
    if check_collision(matrix):
        game_over = True
    for i in range(4):
        sense.set_pixels(flatten(matrix))
        matrix = move_pipes(matrix)
        sense.set_pixel(x,y,YELLOW)
        if check_collision(matrix):
            game_over = True
        sleep(1)
        
sense.show_message('You lose')
sense.clear()
exit()
