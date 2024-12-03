import re, pyperclip

#region Part1
def import_data(current_day):
    global data
    data = open(f"2024\inputs\{current_day}.txt", "r").read()

def initiate_variables():
    global mul_list, total_score, final_list
    mul_list, final_list = [], []
    total_score = 0
    
def create_mul_lists(extraxt_string):
    return re.findall(r"mul\((\d+),(\d+)\)", extraxt_string)
    
def process_mul_matches(mul_match):
    single_digits = list(mul_match)
    return int(single_digits[0]) * int(single_digits[1])
    
import_data("day3")
initiate_variables()
mul_list = create_mul_lists(data)
for mul_match in mul_list:
    total_score += process_mul_matches(mul_match)
print(f"Solution Part 1: {total_score}")

#endregion Part1

#region Part2

def split_string_by_do(extraxt_string):
    extraxt_string = re.sub("\n", "", extraxt_string)
    return list(re.split(r"do\(\)", extraxt_string))

def remove_all_donts(list_part):
    return re.sub(r"don't\(\).*", "", list_part)

initiate_variables()

do_split_string = split_string_by_do(data)

for part in do_split_string:
    mul_list.append(remove_all_donts(part))

for part in mul_list:
    final_list.append(create_mul_lists(part))

for mul_group in final_list:
    for mul in mul_group:
        total_score += process_mul_matches(mul)
print(f"Solution Part 2: {total_score}")

#endregion Part2