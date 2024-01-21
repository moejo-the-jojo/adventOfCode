import re, sys

sys.setrecursionlimit(10000000)

data = open("2023\inputs\day8.txt", "r").read()

lrlr, all_paths = data.split("\n\n")
all_paths_list = all_paths.split("\n")

lrlr = lrlr.replace("R", "1").replace("L", "0")

lrlr = str(list(lrlr).copy())

original_lrlr = list(lrlr)

lrlr = original_lrlr.copy()

counter = -1

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
            global lrlr, counter, original_lrlr
         
            counter += 1
            if len(lrlr) > 0:
                if lrlr.pop(0) == True:
                    return {path_2}()
                else:
                    return {path_1}()
            else:
                lrlr = original_lrlr.copy()
                if lrlr.pop(0) == True:
                    return {path_2}()
                else:
                    return {path_1}()
    """)
    
del ZZZ

def ZZZ():
    global counter
    print(counter)

AAA()

#78, 79, 80 false