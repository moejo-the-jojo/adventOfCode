import re

data = open("2023\inputs\day8.txt", "r").read()

lrlr, all_paths = data.split("\n\n")
all_paths_list = all_paths.split("\n")

lrlr = lrlr.replace("R", "1").replace("L", "0")

original_lrlr = list(lrlr)

lrlr = original_lrlr.copy()

counter = 0


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
    
del ZZZ

def ZZZ():
    pass

curr_function = eval("AAA")

while True:
    next_one = curr_function()
    if next_one == "ZZZ":
        ZZZ()
        break
    curr_function = eval(next_one)

print("solution pt 1:", counter)

lrlr, all_paths = data.split("\n\n")
all_paths_list = all_paths.split("\n")

lrlr = lrlr.replace("R", "1").replace("L", "0")

original_lrlr = list(lrlr)

lrlr = original_lrlr.copy()

counter = 0

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
    
# del ZZZ

# def ZZZ():
#     pass

starting_functions = [eval(x) for x in starting_paths]

print(lrlr)



print(starting_paths)
ajo = 0
lenZ = []
while True:
    if len(lrlr) == 0:
        lrlr = original_lrlr.copy()
    current_lrlr = lrlr.pop(0)
    next_iteration = []
    
    for i in starting_functions:
        next_iteration.append(i())
    counter += 1
    
    lenZ.append(len([x for x in next_iteration if x[2] == "Z"]))

    # if len(next_iteration) == len([x for x in next_iteration if x[2] == "Z"]):
    #     break

    ajo += 1
    if ajo == 10000:
        break
    starting_functions = [eval(x) for x in next_iteration]
    
print(sorted(lenZ, reverse=True))

print(counter)