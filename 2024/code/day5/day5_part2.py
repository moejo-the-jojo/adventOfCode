def import_data(current_day_nr):
    global data
    data = open(f"2024\inputs\day{current_day_nr}\day{current_day_nr}.txt", "r").read()
    
def import_example(current_day_nr):
    global data
    data = open(f"2024\inputs\day{current_day_nr}\day{current_day_nr}_example.txt", "r").read()
    
def initiate_variables():
    global ordering_rules, updates, total_score, right_orders
    ordering_rules, updates, right_orders = [], [], []
    total_score = 0

def prepare_input(raw_input):
    ordering_rules_total, updates_total = raw_input.split("\n\n")
    ordering_rules = ordering_rules_total.split("\n")
    for i in range(len(ordering_rules)):
        ordering_rules[i] = [int(x) for x in ordering_rules[i].split("|")]
    updates = [x.split(",") for x in updates_total.split("\n")]
    for i in range(len(updates)):
        updates[i] = [int(y) for y in updates[i]]
    return ordering_rules, updates
    
def filter_for_relevant_updates(update):
    relevant_ordering_rules = []
    for order in ordering_rules:
        if order[0] in update and order[1] in update:
            relevant_ordering_rules.append(order)
    return relevant_ordering_rules
    
def create_must_be_right_dict(relevant_ordering_rules):
    must_be_right_dict = {}
    for order in relevant_ordering_rules:
        try:
            must_be_right_dict[order[0]].append(order[1])
        except:        
            must_be_right_dict[order[0]] = [order[1]]
    return must_be_right_dict

def create_complete_order(must_be_right_dict):
    lessamakealist = list(must_be_right_dict.items())
    lessamakealist.sort(key = lambda x: len(x[1]), reverse= True)
    last_value = lessamakealist[-1][1]
    return [x[0] for x in lessamakealist] + last_value

def check_validity(complete_order, update):
    index_of_order = [complete_order.index(x) for x in update]
    if sorted(index_of_order) != index_of_order:
        return True


# import_example(5)

import_data(5)

initiate_variables()

ordering_rules, updates = prepare_input(data)


for update in updates:
    relevant_ordering_rules = filter_for_relevant_updates(update)
    
    must_be_right_dict = create_must_be_right_dict(relevant_ordering_rules)
        
    complete_order = create_complete_order(must_be_right_dict)
    
    if check_validity(complete_order, update) == True:
        right_orders.append(complete_order)

for correct_order in right_orders:
    total_score += correct_order[int(len(correct_order)/2)]
    
print(f"Solution Part 2: {total_score}")