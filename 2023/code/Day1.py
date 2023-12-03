import re

data = open("2023\inputs\day1.txt", "r").read()

sum_pt1 = 0
sum_pt2 = 0
single_line = data.split("\n")
numbs_dic = {"one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r", "five": "f5e", "six": "s6x", "seven": "s7n", "eight": "e8t", "nine": "n9e"}

for line in single_line:
    curr_numbs = [int(x) for x in line if x.isnumeric()]
    sum_pt1 += int(str(curr_numbs[0]) + str(curr_numbs[-1]))

print(f"Solution pt1: {sum_pt1}")

for line in single_line:
    pattern = re.compile(r"(one|two|three|four|five|six|seven|eight|nine)")
    while re.search(pattern, line):
        line = re.sub(pattern, lambda x: numbs_dic[x.group()], line)
    curr_numbs = [int(x) for x in line if x.isnumeric()]
    sum_pt2 += int(str(curr_numbs[0]) + str(curr_numbs[-1]))

print(f"Solution pt2: {sum_pt2}")