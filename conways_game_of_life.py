# A simpler form of Conway's Game of life
# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

from copy import deepcopy


# the initial data of the cells
# "X" represents an organism
# "-" represents an empty cell

initial_data = "XXX--X-,--XX-X-,-X-XX--,-X-X-XX,XX-XX-X"

# you can select number of turns from here
number_of_turn = 5

# each row elements from the initial data
initial_config = initial_data.split(",")

# number of rows and number of columns in the initial_config
num_row = len(initial_config)
num_col = len(initial_config[1])


# creating a grid of position dictionary
living_area = {}
for i in range(3*num_row):  # the row of the grid will be the 3 times larger
    for j in range(3*num_col):  # the column of the grid will be the 3 times larger
        living_area[(i, j)] = 0  # initial status of the grid


# appending the organism structure into the grid
for i in range(num_row):
    for j in range(num_col):
        if initial_config[i][j] == "-":
            # if the cell does not contain an organism
            living_area[(i + num_row, j + num_col)] = 0
        else:
            # if the cell contains an organism
            living_area[(i + num_row, j + num_col)] = 1


def distance_sqrd(p1, p2):
    return (p1[1] - p2[1])**2 + (p1[0] - p2[0])**2


def organism_counter(cell_pos, test_dict):
    """takes the position of the cell and the current status of the living area
    as an output in returns the number of the organisms near the given cell"""
    neighbours = []
    alive_organism = 0
    for loc in test_dict.keys():
        if distance_sqrd(loc, cell_pos) == 1 or distance_sqrd(loc, cell_pos) == 2:
            neighbours.append(loc)
    for nghb in neighbours:
        if test_dict[nghb] == 1:  # if the neighbour of the cell contains an organism
            alive_organism += 1
    return alive_organism  # return the total number of organisms w.r.t cell position


def total_organism_counter(test_dict):
    values = test_dict.values()
    return sum(values)


def printing_formatter(test_dict):
    condensed = ""
    for val in test_dict.values():
        if val == 1:
            condensed += "X"
        else:
            condensed += "-"
    for i in range(3 * num_row):
        print(condensed[3 * num_col * i: 3 * num_col*(i + 1)])


for i in range(number_of_turn):
    updating_area = deepcopy(living_area)
    for cell in living_area.keys():  # for each cell in the matrix
        if living_area[cell] == 0:  # if the cell does not contain an organism
            # if the cells nearby have 3 living organism
            if organism_counter(cell, living_area) == 3:
                updating_area[cell] = 1  # a new organism is born
        if living_area[cell] == 1:  # if the cell contains an organism
            if organism_counter(cell, living_area) < 2 or organism_counter(cell, living_area) > 3:
                updating_area[cell] = 0  # the organism dies
            else:
                updating_area[cell] = 1  # the organism lives
    total_organism = total_organism_counter(updating_area)
    printing_formatter(updating_area)
    print("Number of total organism:", total_organism, "\n")
    living_area = updating_area
