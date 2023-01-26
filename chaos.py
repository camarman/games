# https://en.wikipedia.org/wiki/Chaos_game
# Chaos Game for equilateral triangle, square and equilateral pentagon

from random import randint
from turtle import *


screensize(2000, 2000)
screen = Screen()
screen.title('Chaos Game')
pencolor('red')
speed(0)

# the shape of the object as triangle (3), square(4) and pentagon(5)
shape = screen.numinput(
    'Geometric Shape', 'Enter the corner number of the shape (3-5)', default=3, minval=3, maxval=5)

if shape == 3:
    side_len = screen.numinput('Side Length', 'Enter the side length of the equilateral triangle (100-700):', 200, 100, 700)
elif shape == 4:
    side_len = screen.numinput('Side Length', 'Enter the side length of the square (100-700):', 200, 100, 700)
elif shape == 5:
    side_len = screen.numinput('Side Length', 'Enter the side length of the equilateral pentagon (100-700):', 200, 100, 700)


if shape == 3:
    # drawing the corners (A - B - C) of the equilateral triangle
    penup()
    forward(side_len)
    dot(9)
    A = position()  # corner points of the equilateral triangle
    left(120)
    forward(side_len)
    dot(9)
    B = position()
    left(120)
    forward(side_len)
    dot(9)
    C = position()
    # taking the initial point as an input
    init_pos_x = screen.numinput('Initial Point', 'Enter the x-coordinate of the starting point:', int(side_len//2), 0, 1000)
    init_pos_y = screen.numinput('Initial Point', 'Enter the y-coordinate of the starting point:', int(side_len//2), 0, 1000)
    goto(init_pos_x, init_pos_y)
    pos = position() # recording the initial position of the point
    dot(9, "blue")
    while True:
        die_num = randint(1, 6)
        if die_num == 1 or die_num == 2:
            new_pos_x = (pos[0] + A[0]) / 2   # measuring the new position
            new_pos_y = (pos[1] + A[1]) / 2
            goto(new_pos_x, new_pos_y)
            dot(6, "black")
            pos = position()  # recording this new position
        if die_num == 3 or die_num == 4:
            new_pos_x = (pos[0] + B[0]) / 2
            new_pos_y = (pos[1] + B[1]) / 2
            goto(new_pos_x, new_pos_y)
            dot(6, "black")
            pos = position()
        if die_num == 5 or die_num == 6:
            new_pos_x = (pos[0] + C[0]) / 2
            new_pos_y = (pos[1] + C[1]) / 2
            goto(new_pos_x, new_pos_y)
            dot(6, "black")
            pos = position()


if shape == 4:
    # drawing the corners (A - B - C - D) of the square
    penup()
    forward(side_len)
    A = position()
    dot(9)
    right(90)
    forward(side_len)
    B = position()
    dot(9)
    right(90)
    forward(side_len)
    C = position()
    dot(9)
    right(90)
    forward(side_len)
    D = position()
    dot(9)
    # taking the initial point as an input
    init_pos_x = screen.numinput('Initial Point', 'Enter the x-coordinate of the starting point:', int(side_len//2), 0, 1000)
    init_pos_y = screen.numinput('Initial Point', 'Enter the y-coordinate of the starting point:', int(side_len//2), 0, 1000)
    goto(init_pos_x, init_pos_y)
    pos = position()
    dot(9, "blue")
    g = 0
    w1 = [1, 2]
    w2 = [3, 4]
    w3 = [5, 6]
    w4 = [7, 8]
    while True:
        w = randint(1, 8)
        if w in w1 and g not in w1:
            new_pos_x = (pos[0] + A[0]) / 2  # measuring the new position
            new_pos_y = (pos[1] + A[1]) / 2
            goto(new_pos_x, new_pos_y)
            dot(6, "black")
            pos = position()  # recording this new position
        if w in w2 and g not in w2:
            new_pos_x = (pos[0] + B[0]) / 2
            new_pos_y = (pos[1] + B[1]) / 2
            goto(new_pos_x, new_pos_y)
            dot(6, "black")
            pos = position()
        if w in w3 and g not in w3:
            new_pos_x = (pos[0] + C[0]) / 2
            new_pos_y = (pos[1] + C[1]) / 2
            goto(new_pos_x, new_pos_y)
            dot(6, "black")
            pos = position()
        if w in w4 and g not in w4:
            new_pos_x = (pos[0] + D[0]) / 2
            new_pos_y = (pos[1] + D[1]) / 2
            goto(new_pos_x, new_pos_y)
            dot(6, "black")
            pos = position()
        g = w


if shape == 5:
    # drawing the corners (A - B - C - D - E) of the equilateral pentagon
    penup()
    forward(side_len)
    A = position()
    dot(9)
    right(72)
    forward(side_len)
    B = position()
    dot(9)
    right(72)
    forward(side_len)
    C = position()
    dot(9)
    right(72)
    forward(side_len)
    D = position()
    dot(9)
    right(72)
    forward(side_len)
    E = position()
    dot(9)
    # taking the initial point as an input
    init_pos_x = screen.numinput('Initial Point', 'Enter the x-coordinate of the starting point:', int(side_len//2), 0, 1000)
    init_pos_y = screen.numinput('Initial Point', 'Enter the y-coordinate of the starting point:', int(side_len//2), 0, 1000)
    goto(init_pos_x, init_pos_y)
    pos = position()
    dot(9, "blue")
    g = 0
    w1 = [1, 2]
    w2 = [3, 4]
    w3 = [5, 6]
    w4 = [7, 8]
    w5 = [9, 10]
    while True:
        w = randint(1, 10)
        if w in w1 and g not in w1:
            new_pos_x = (pos[0] + A[0]) / 2  # measuring the new position
            new_pos_y = (pos[1] + A[1]) / 2
            goto(new_pos_x, new_pos_y)
            dot(6, "black")
            pos = position()  # recording this new position
        if w in w2 and g not in w2:
            new_pos_x = (pos[0] + B[0]) / 2
            new_pos_y = (pos[1] + B[1]) / 2
            goto(new_pos_x, new_pos_y)
            dot(6, "black")
            pos = position()
        if w in w3 and g not in w3:
            new_pos_x = (pos[0] + C[0]) / 2
            new_pos_y = (pos[1] + C[1]) / 2
            goto(new_pos_x, new_pos_y)
            dot(6, "black")
            pos = position()
        if w in w4 and g not in w4:
            new_pos_x = (pos[0] + D[0]) / 2
            new_pos_y = (pos[1] + D[1]) / 2
            goto(new_pos_x, new_pos_y)
            dot(6, "black")
            pos = position()
        if w in w5 and g not in w5:
            new_pos_x = (pos[0] + E[0]) / 2
            new_pos_y = (pos[1] + E[1]) / 2
            goto(new_pos_x, new_pos_y)
            dot(6, "black")
            pos = position()
        g = w
