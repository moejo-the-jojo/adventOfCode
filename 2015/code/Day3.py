data = open("2015/inputs/day3.txt", "r").read()

position = [0,0]

visited_houses = [(position[0], position[1])]

for move in data:
    match move:
        case "^":
            position[1] += 1
        case "v":
            position[1] -=1
        case "<":
            position[0] -= 1
        case ">":
            position[0] += 1
    if (position[0], position[1]) in visited_houses:
        continue
    else:
        visited_houses.append((position[0], position[1]))

print("part 1 solution: " + str(len(visited_houses)))

santa = [0,0]
robo = [0,0]

all_houses = [(santa[0], santa[1])]

for who, move in enumerate(data):
    if who % 2 == 0:
        current = [santa[0], santa[1]]
    else:
        current = [robo[0], robo[1]]
    match move:
        case "^":
            current[1] += 1
        case "v":
            current[1] -= 1
        case "<":
            current[0] -= 1
        case ">":
            current[0] += 1
    if who % 2 == 0:
        santa = [current[0], current[1]]
    else:
        robo = [current[0], current[1]]
    if (current[0], current[1]) in all_houses:
        continue
    else:
        all_houses.append((current[0], current[1]))

print("part 2 solution: " + str(len(all_houses)))