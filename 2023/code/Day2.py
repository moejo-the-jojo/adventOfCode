import re

data = open("2023\inputs\day2.txt", "r").read()

single_line = data.split("\n")

numbers_pattern = re.compile(r"\d+")
green = re.compile(r"(\d+)\sgreen")
red = re.compile(r"(\d+)\sred")
blue = re.compile(r"(\d+)\sblue")
sum = 0

for line in single_line:
    impossible = False
    id = re.search(numbers_pattern, line)
    games = line.split(":")[1]
    single_games = games.split(";")
    for curr_game in single_games:
        try:
            green_count = re.findall(green, curr_game)[0]
        except:
            green_count = 0
        try:
            blue_count = re.findall(blue, curr_game)[0]
        except:
            blue_count = 0
        try:
            red_count = re.findall(red, curr_game)[0]
        except:
            red_count = 0
        if int(green_count) > 13 or int(blue_count) > 14 or int(red_count) > 12:
            impossible = True
            break
    if impossible == False:
        sum += int(id[0])

print(f"solution part 1: {sum}")

sum_pt2 = 0

for line in single_line:
    games = line.split(":")[1]
    blue_count, red_count, green_count = 0, 0, 0
    final_blue_count, final_red_count, final_green_count = 0, 0, 0
    single_games = games.split(";")

    for curr_game in single_games:
        try:
            green_count = int(re.findall(green, curr_game)[0])
        except:
            green_count = 0
        try:
            blue_count = int(re.findall(blue, curr_game)[0])
        except:
            blue_count = 0
        try:
            red_count = int(re.findall(red, curr_game)[0])
        except:
            red_count = 0
        if green_count > final_green_count:
            final_green_count = green_count
        if red_count > final_red_count:
            final_red_count = red_count
        if blue_count > final_blue_count:
            final_blue_count = blue_count
    sum_pt2 += (final_blue_count * final_red_count * final_green_count)

print(f"Solution pt 2: {sum_pt2}")