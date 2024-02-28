import re
import math

data = open("2023\inputs\day8.txt", "r").read()

lrlr, all_paths = data.split("\n\n")
all_paths_list = all_paths.split("\n")

lrlr = lrlr.replace("R", "1").replace("L", "0")

original_lrlr = list(lrlr).copy()

lrlr = original_lrlr.copy()

counter = 1


for path in all_paths_list:
    start, path_1, path_2 = re.findall(r"\w+", path)

    exec(f"""def {start}():
            global lrlr, counter, original_lrlr, next_step
            next_step = lrlr.pop(0)
            counter += 1
            if len(lrlr) > 0:
                if int(next_step) == 1:
                    return "{path_2}"
                else:
                    return "{path_1}"
            else:
                lrlr = original_lrlr.copy()
                if int(next_step) == 1:
                    return "{path_2}"
                else:
                    return "{path_1}"
    """)
    
curr_function = eval("AAA")

while True:
    next_one = curr_function()
    if next_one == "ZZZ":
        break
    curr_function = eval(next_one)

print("solution pt 1:", counter-1)


lrlr, all_paths = data.split("\n\n")
all_paths_list = all_paths.split("\n")

lrlr = lrlr.replace("R", "1").replace("L", "0")

original_lrlr = list(lrlr)

lrlr = original_lrlr.copy()

counter = 1

starting_paths = []

for path in all_paths_list:
    start, path_1, path_2 = re.findall(r"\w+", path)

    if start[2] == "A":
        starting_paths.append(start)

    exec(f"""def {start}():
            global current_lrlr
            if int(current_lrlr) == 1:
                return "{path_2}"
            else:
                return "{path_1}"
            
    """)
    
starting_functions = [eval(x) for x in starting_paths]

lenZ = []
steps_to_Z = []

while len(starting_functions) > 0:
    if len(lrlr) == 0:
        lrlr = original_lrlr.copy()
    current_lrlr = lrlr.pop(0)
    
    next_iteration = []
    
    for i in starting_functions:
        j = i()
        if j[2] == "Z":
            steps_to_Z.append(counter)
        else:
            next_iteration.append(j)
    counter += 1
    
    starting_functions = [eval(x) for x in next_iteration]

print("solution pt 2: " + str(math.lcm(*steps_to_Z)))