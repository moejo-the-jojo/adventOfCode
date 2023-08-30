data = open("2015\inputs\day1.txt", "r").read()

count_up = 0
count_down = 0

for i in data:
    if i == "(":
        count_up += 1
    elif i == ")":
        count_down += 1

print("part 1 solution: " + str(count_up-count_down))


count_general = 0
steps = 0

for i, j in enumerate(data):
    if j == "(":
        count_general += 1
    elif j == ")":
        count_general -= 1
    if count_general < 0:
        steps = i
        break

print("part 2 solution: " + str(steps + 1))