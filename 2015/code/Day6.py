import re

data = open("2015/inputs/day6.txt", "r").read()

single_commands = data.split("\n")[:-1]

grid = []

for i in range(1000):
    grid.append([False]*1000)

for command in single_commands:
    lightning_move = re.findall(r"^\D*", command)[0]
    lightning_move = lightning_move.replace(" ", "")
    start_y, start_x, stop_y, stop_x = re.findall(r"\d+", command)

    for i in range(int(start_x), int(stop_x)+1):
        for j in range(int(start_y), int(stop_y)+1):
            match lightning_move:
                case "turnon":
                    grid[i][j] = True
                case "turnoff":
                    grid[i][j] = False
                case "toggle":
                    grid[i][j] = not grid[i][j]

print("part 1 solution: " + str(sum([sum(row) for row in grid])))

brightness_grid = []

for i in range(1000):
    brightness_grid.append([0]*1000)

for command in single_commands:
    lightning_move = re.findall(r"^\D*", command)[0]
    lightning_move = lightning_move.replace(" ", "")
    start_y, start_x, stop_y, stop_x = re.findall(r"\d+", command)

    for i in range(int(start_x), int(stop_x)+1):
        for j in range(int(start_y), int(stop_y)+1):
            match lightning_move:
                case "turnon":
                    brightness_grid[i][j] += 1
                case "turnoff":
                    if brightness_grid[i][j] == 0:
                        continue
                    else:
                        brightness_grid[i][j] -= 1
                case "toggle":
                    brightness_grid[i][j] += 2

print("part 2 solution: " + str(sum([sum(row) for row in brightness_grid])))