def import_data(current_day_nr):
    global data
    data = open(f"2024\inputs\day{current_day_nr}\day{current_day_nr}.txt", "r").read()
    
def import_example(current_day_nr):
    global data
    data = open(f"2024\inputs\day{current_day_nr}\day{current_day_nr}_example.txt", "r").read()

def initiate_variables():
    global keep_going, current_direction, visited_coords, current_coords, all_directions, loop_detected
    keep_going = True
    all_directions = [[-1,0], [0,1], [1,0], [0,-1]]
    current_direction = [-1,0]
    current_coords, visited_coords = [], []
    loop_detected = 0

def prepare_input(input):
    listed_input = input.split("\n")
    padded_input = [["W"] + list(x) + ["W"] for x in listed_input]
    new_line = [["W"] * len(padded_input[0])]
    return new_line + padded_input + new_line

def find_starting_point():
    global matrix
    for x_coord, line in enumerate(matrix):
        for y_coord, letter in enumerate(line):
            if letter == "^":
                matrix[x_coord][y_coord] = "."
                return x_coord, y_coord

def check_next_field():
    global matrix, visited_coords, keep_going, current_direction, current_coords, all_directions, loop_detected
    next_field = matrix[current_coords[0] + current_direction[0]][current_coords[1] + current_direction[1]]
    if len(visited_coords) >= 7000:
        keep_going = False
        loop_detected = 1
        return
    visited_coords.append((current_coords[0], current_coords[1]))
    if next_field == "W":
        keep_going = False
        loop_detected = 0
        # print(visited_coords)
        return
    elif next_field == ".":
        current_coords[0] += current_direction[0]
        current_coords[1] += current_direction[1]
        return
    else:
        index = all_directions.index(current_direction)
        current_direction = all_directions[(index + 1)%4]
        return



# import_example(6)

import_data(6)

initiate_variables()

total_score = 0

matrix = prepare_input(data)

starting_x, starting_y = find_starting_point()

current_coords.append(starting_x)
current_coords.append(starting_y)

starting_poing = current_coords.copy()

for x_coord, line in enumerate(matrix):
    for y_coord, letter in enumerate(line):
        prev_matrix_val = matrix[x_coord][y_coord]
        if letter == ".":
            matrix[x_coord][y_coord] = "#"
        while keep_going == True:
            check_next_field()
        total_score += loop_detected
        initiate_variables()
        current_coords = starting_poing.copy()
        matrix[x_coord][y_coord] = prev_matrix_val

print(f"Solution Part 1: {total_score}")