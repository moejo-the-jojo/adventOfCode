def import_data(current_day):
    global data
    data = open(f"2024\inputs\{current_day}\{current_day}.txt", "r").read()
    
def import_example(current_day):
    global data
    data = open(f"2024\inputs\{current_day}\{current_day}_example.txt", "r").read()
    
def initiate_variables():
    global xmas_example, total_score
    xmas_example = ["X", "M", "A", "S"]
    total_score = 0
    
def prepare_input(input):
    listed_input = input.split("\n")
    listed_input = [["P", "P", "P"] + list(x) + ["P", "P", "P"] for x in listed_input]
    new_line = [["P"] * len(listed_input[0])]
    return new_line*3 + listed_input + new_line *3

def find_xmas(x_coord, y_coord):
    score_for_current_x = 0
    for x in range(-1,2):
        for y in range(-1, 2):
            if starting_input[x_coord + x][y_coord + y] == xmas_example[1]:
                score_for_current_x += follow_the_mas(x_coord, y_coord, x, y)
    return score_for_current_x
            
def follow_the_mas(start_x, start_y, delta_x, delta_y):
    xmas_fully_there = []
    for index in range(0, 4):
        xmas_fully_there += starting_input[start_x + delta_x * index][start_y + delta_y *index]
    if xmas_fully_there == xmas_example:
        return 1
    else:
        return 0




import_data("day4")
# import_example("day4")
starting_input = prepare_input(data)
initiate_variables()
for x_coord, line in enumerate(starting_input):
    for y_coord, letter in enumerate(line):
        if letter == "X":
            total_score += find_xmas(x_coord, y_coord)
            
print(f"Solution part 1: {total_score}")