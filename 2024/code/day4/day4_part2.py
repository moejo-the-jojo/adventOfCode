def import_data(current_day):
    global data
    data = open(f"2024\inputs\{current_day}\{current_day}.txt", "r").read()
    
def import_example(current_day):
    global data
    data = open(f"2024\inputs\{current_day}\{current_day}_example.txt", "r").read()
    
def initiate_variables():
    global total_score
    total_score = 0
    
def prepare_input(input):
    listed_input = input.split("\n")
    listed_input = [["P", "P", "P"] + list(x) + ["P", "P", "P"] for x in listed_input]
    new_line = [["P"] * len(listed_input[0])]
    return new_line*3 + listed_input + new_line *3

def find_xmas(x_coord, y_coord):
    corner_letters = []
    for x in [-1, 1]:
        for y in [-1, 1]:
            corner_letters.append(starting_input[x_coord + x][y_coord + y])
    if sorted(corner_letters) == ["M", "M", "S", "S"] and starting_input[x_coord-1][y_coord-1] != starting_input[x_coord+1][y_coord+1]:
        return 1
    else:
        return 0



import_data("day4")

# import_example("day4")

starting_input = prepare_input(data)

initiate_variables()

for x_coord, line in enumerate(starting_input):
    for y_coord, letter in enumerate(line):
        if letter == "A":
            total_score += find_xmas(x_coord, y_coord)
            
print(f"Solution part 2: {total_score}")