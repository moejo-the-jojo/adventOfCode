import re

data = open("2015/inputs/day6.txt", "r").read()

single_commands = data.split("\n")

grid = []

for i in range(1000):
    grid.append([False]*1000)

for command in single_commands:
    lightning_move = re.findall(r"^\D*", command)[0]
    lightning_move = lightning_move.replace(" ", "")

    