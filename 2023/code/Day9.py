data = open("2023/inputs/day9.txt", "r").read()

lines = data.split("\n")
lines = list(map(lambda x: x.split(" "), lines))

int_lines = []
for i in lines:
    int_lines.append([int(x) for x in i])

# print(int_lines)

sum = 0

for original_line in int_lines:
    calculation_list = [original_line]
    zauber = 0
    while True:
        if calculation_list[-1][0] == 0 and calculation_list[-1][1] == 0:
            break
        temp = []
        for element in range(len(calculation_list[-1])-1):
            temp.append(calculation_list[-1][element+1] - calculation_list[-1][element])
        calculation_list.append(temp)


    while len(calculation_list) > 1:
        last_one = calculation_list.pop()
        calculation_list[-1].append(calculation_list[-1][-1] + last_one[-1])

    print(calculation_list[-1][-1])
    sum += calculation_list[-1][-1]

print(sum)

#1782889025 too high
#1744890533 too low