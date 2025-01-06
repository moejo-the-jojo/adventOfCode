import itertools

def import_data(current_day_nr):
    global data
    data = open(f"2024\inputs\day{current_day_nr}\day{current_day_nr}.txt", "r").read()
    
def import_example(current_day_nr):
    global data
    data = open(f"2024\inputs\day{current_day_nr}\day{current_day_nr}_example.txt", "r").read()

def initiate_variables():
    global total_score
    total_score = 0
    
def prepare_input(data):
    data = data.split("\n")
    data = data[5:]
    all_equations = []
    for line in data:
        check_value = line.split(":")[0]
        operands_half = line.split(":")[1]
        raw_operands = operands_half.split(" ")
        operands = [int(x) for x in raw_operands[1:]]
        all_equations.append([check_value, operands])
    return all_equations

def check_equation(equation):
    check_value = equation[0]
    operands = equation[1]
    empty_places = len(operands) -1
    total_combinations = []
    total_results = []
    comb = list(itertools.combinations_with_replacement(["+", "*"], empty_places))
    for i in comb:
        single_comb = list(itertools.permutations(i))
        for j in single_comb:
            if j not in total_combinations:
                total_combinations.append(j)
    for combination in total_combinations:
        calculation = []
        for i in range(0, empty_places):
            calculation.append(operands[i])
            calculation.append(combination[i])
        calculation.append(operands[-1])
        while len(calculation) >= 3:
            current_bit = calculation[0:3]
            current_bit = [str(x) for x in current_bit]
            new_result = eval("".join(current_bit))
            try:
                calculation = [new_result, *calculation[3:]]
            except:
                break
            print(calculation)
        if calculation not in total_results:
            total_results.append(calculation[0])
    if (int(check_value) in total_results):
        return 1
    else:
        return 0
            
import_data(7)

# import_example(7)

initiate_variables()

all_equations = prepare_input(data)

for equation in all_equations:
    global total_score
    print(equation)
    total_score += check_equation(equation)
    print(total_score)
print(total_score)