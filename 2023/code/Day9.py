data = open("2023/inputs/day9.txt", "r").read()

lines = data.split("\n")
lines = list(map(lambda x: x.split(" "), lines))

int_lines = []
for i in lines:
    int_lines.append([int(x) for x in i])

sum = 0

for original_line in int_lines:
    calculation_list = [original_line]
    while calculation_list[-1][0] != 0 or calculation_list[-1][1] != 0:
        temp = []
        for number_in_list in range(len(calculation_list[-1])-1):
            temp.append(calculation_list[-1][number_in_list+1] - calculation_list[-1][number_in_list])
        calculation_list.append(temp)
    
    while len(calculation_list) > 1:
        last_one = calculation_list.pop()
        calculation_list[-1].append(calculation_list[-1][-1] + last_one[-1])


    sum += calculation_list[-1][-1]

print("Solution: " + str(sum))

#"1782889025" is too high