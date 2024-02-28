data = open("2023/inputs/day9.txt", "r").read()

lines = data.split("\n")
lines = list(map(lambda x: x.split(" "), lines))

int_lines = []
for i in lines:
    int_lines.append([int(x) for x in i])

# print(int_lines)


for i in int_lines[0:1]:
    print(i)
    calculation_list = []
    temp = []
    for index, j in enumerate(i):
        if index+2 > len(i):
            break
        temp.append(int(*i[index+1:index+2]) - j)

    print(temp)