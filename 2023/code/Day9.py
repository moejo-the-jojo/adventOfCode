# get data and process it
def get_data(filename):
    data = open(filename, "r").read()

    split_in_lines = data.split("\n")
    split_each_line_in_numbers = list(map(lambda x: x.split(" "), split_in_lines))
    ever_number_is_an_int_now = [[int(x) for x in pre_int_line] for pre_int_line in split_each_line_in_numbers]

    return ever_number_is_an_int_now

# calculate the next number in a list
def calculate_next_number(history):
    # create new lists with differences of last list until the appended list contains only 0
    calculation_list = [history]
    while calculation_list[-1][0] != 0 or calculation_list[-1][-1] != 0:
        temp = []
        for number_in_list in range(len(calculation_list[-1])-1):
            temp.append(calculation_list[-1][number_in_list+1] - calculation_list[-1][number_in_list])
        calculation_list.append(temp)
    # add next number to all lists of differences, and finally to original list
    while len(calculation_list) > 1:
        last_list = calculation_list.pop()
        last_number_in_last_list = last_list[-1]
        calculation_list[-1].append(calculation_list[-1][-1] + last_number_in_last_list)
    
    # return the result
    return calculation_list[-1][-1]

# add numbers to sum
def sum_results(result):
    global sum
    sum += result


all_lines = get_data("2023/inputs/day9.txt")
sum = 0

for single_line in all_lines:
    next_value = calculate_next_number(single_line)
    sum_results(next_value)

print(f"Solution: {sum}")