data = open("2023\inputs\day3.txt", "r").read()

single_line = data.split("\n")

gen_sum = 0

for index, line in enumerate(single_line):
    single_line[index] = "." + single_line[index] + "."

single_line.insert(0, "."*(len(single_line[0])+1))
single_line.append("."*(len(single_line[0])+1))


for index, line in enumerate(single_line):
    curr_number_coordinates = []
    curr_number = ""
    for indexx, char in enumerate(line):
        if char.isnumeric():
            curr_number_coordinates.append([index, indexx])
            curr_number += str(char)
        else:
            if len(curr_number_coordinates) > 0:
                adjacent_string = ""
                for number_index, coordinates in enumerate(curr_number_coordinates): #eg [0,0], [0,1], [0,2]
                    # top_left:
                    adjacent_string += single_line[coordinates[0]-1][coordinates[1]-1]
                    #top_middle:
                    adjacent_string += single_line[coordinates[0]-1][coordinates[1]]
                    #top_right:
                    adjacent_string += single_line[coordinates[0]-1][coordinates[1]+1]
                    #middle-left:
                    if number_index == 0 and coordinates[1] != 0:
                        adjacent_string += line[coordinates[1]-1]
                    #middle-right:
                    if number_index == len(curr_number_coordinates)-1:
                        adjacent_string += line[coordinates[1]+1]
                    #bottom-left:
                    adjacent_string += single_line[coordinates[0]+1][coordinates[1]-1]
                    #bottom-middle:
                    adjacent_string += single_line[coordinates[0]+1][coordinates[1]]
                    #bottom-right:
                    adjacent_string += single_line[coordinates[0]+1][coordinates[1]+1]
                adjacent_string = adjacent_string.replace(".", "")
                if len(adjacent_string) != 0 and curr_number != "":
                    gen_sum += int(curr_number)
                curr_number = ""
                curr_number_coordinates = []
            else:
                pass

print("Solution part 1: " + str(gen_sum))

gear_middles = []

gear_power_sum = 0

for x, line in enumerate(single_line):
    for y, char in enumerate(line):
        if char == "*":
            gear_middles.append([x, y])

for gear in gear_middles:
    number_of_numbers = 0
    adjacent_list = []
    adjacent_list.append([single_line[gear[0]-1][gear[1]-1], [gear[0]-1, gear[1]-1]])
    adjacent_list.append([single_line[gear[0]-1][gear[1]], [gear[0]-1, gear[1]]])
    adjacent_list.append([single_line[gear[0]-1][gear[1]+1], [gear[0]-1, gear[1]+1]])
    adjacent_list.append([single_line[gear[0]][gear[1]-1], [gear[0], gear[1]-1]])
    adjacent_list.append([single_line[gear[0]][gear[1]+1], [gear[0], gear[1]+1]])
    adjacent_list.append([single_line[gear[0]+1][gear[1]-1], [gear[0]+1, gear[1]-1]])
    adjacent_list.append([single_line[gear[0]+1][gear[1]], [gear[0]+1, gear[1]]])
    adjacent_list.append([single_line[gear[0]+1][gear[1]+1], [gear[0]+1, gear[1]+1]])
    if adjacent_list[0][0].isnumeric() and adjacent_list[1][0].isnumeric() == False and adjacent_list[2][0].isnumeric():
        number_of_numbers += 2
    elif adjacent_list[0][0].isnumeric() or adjacent_list[1][0].isnumeric() or adjacent_list[2][0].isnumeric():
        number_of_numbers += 1
    if adjacent_list[3][0].isnumeric():
        number_of_numbers += 1
    if adjacent_list[4][0].isnumeric():
        number_of_numbers += 1
    if adjacent_list[5][0].isnumeric() and adjacent_list[6][0].isnumeric() == False and adjacent_list[7][0].isnumeric():
        number_of_numbers += 2
    elif adjacent_list[5][0].isnumeric() or adjacent_list[6][0].isnumeric() or adjacent_list[7][0].isnumeric():
        number_of_numbers += 1
    
    if number_of_numbers == 2:
        adjacent_list = [x for x in adjacent_list if x[0].isnumeric()]
        total_rdy_numbers = []
        for number in adjacent_list:
            final_numbers = f"{number[0]}"
            count = 1
            while True:
                if single_line[number[1][0]][number[1][1]-count].isnumeric():
                    final_numbers = str(single_line[number[1][0]][number[1][1]-count]) + final_numbers
                    count += 1
                else:
                    break
            count = 1
            while True:
                if single_line[number[1][0]][number[1][1]+count].isnumeric():
                    final_numbers += str(single_line[number[1][0]][number[1][1]+count])
                    count += 1
                else:
                    break
            total_rdy_numbers.append(int(final_numbers))
        final_numbers = list(dict.fromkeys(total_rdy_numbers))
        gear_power_sum += (final_numbers[0] * final_numbers[1])

print("Solution pt 2: " + str(gear_power_sum))
#80703636