def import_data():
    global data, listed_data
    data = open("2024\inputs\day1.txt", "r").read()

    listed_data = data.split("\n")


def initiate_variables():
    global left_list, right_list, total_distance
    left_list, right_list = [], []
    total_distance = 0

def prepare_lists():
    global left_list, right_list
    for line in listed_data:
        left_number, right_number = line.split("   ")
        left_list.append(int(left_number))
        right_list.append(int(right_number))

    left_list.sort()
    right_list.sort()

def calculate_sum():
    global total_distance, left_list, right_list
    for i in range(0, len(left_list)):
        total_distance += abs(left_list[i]-right_list[i])

def calculate_second_day():
    global total_distance, left_list, right_list
    
    for i in range(0, len(left_list)):
        total_distance += left_list[i]*right_list.count(left_list[i])
    return total_distance

import_data()

initiate_variables()
prepare_lists()
calculate_sum()
print(f"Solution Day 1: {total_distance}")


initiate_variables()
prepare_lists()
calculate_second_day()
print(f"Solution Day 2: {total_distance}")
