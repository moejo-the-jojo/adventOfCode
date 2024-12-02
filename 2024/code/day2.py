def import_data(file_location):
    global data, listed_data
    data = open(file_location, "r").read()

    listed_data = data.split("\n")


def intiate_variables():
    global report_list, valid_range_scores, valid_total_scores
    report_list = []
    valid_range_scores = []
    valid_total_scores = 0
    
def prepare_inputs():
    global report_list
    for line in listed_data:
        report_list.append(list(int(x) for x in line.split(" ")))
        
def score_scored(list):
    fail_count = 0
    direction = ""
    og_list = list.copy()
    
    if list[0] - list[-1] > 0:
        direction = "descending"
    else:
        direction = "ascending"
    
    if direction == "ascending":
        for i in range(0, len(og_list)):
            del(list[i])
            for number in range(0, len(list)-1):
                prev, next = int(list[number:number+1][0]), int(list[number+1:number+2][0])
                if (prev >= next or abs(prev - next) > 3):
                    fail_count += 1
            if fail_count == 0:
                return 1
            else:
                fail_count = 0
                list = og_list.copy()
    else:
        for i in range(0, len(og_list)):
            del(list[i])
            for number in range(0, len(list)-1):
                prev, next = int(list[number:number+1][0]), int(list[number+1:number+2][0])
                if (prev <= next or abs(prev - next) > 3):
                    fail_count += 1
            if fail_count == 0:
                return 1
            else:
                fail_count = 0
                list = og_list.copy()
            
    return 0

    
import_data("2024\inputs\day2.txt")
intiate_variables()
prepare_inputs()
for report in report_list:
    valid_total_scores += score_scored(report)
print(f"Solution Part 2: {valid_total_scores}")