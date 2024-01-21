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
    # def start():
    #      global lrlr
    #      if lrlr.pop() == True:
    #         return path_1()
    #     else:
    #         return path_2()

            # print({start, path_1, path_2})


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
    global counter
    print(counter)

curr_function = eval("AAA")

# print(lrlr)


while True:
    next_one = curr_function()
    if next_one == "ZZZ":
        ZZZ()
        break
    curr_function = eval(next_one)

print("solution pt 1:", counter)