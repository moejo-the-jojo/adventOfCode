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