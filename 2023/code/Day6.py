data = open("2023\inputs\day6.txt", "r").read()

time, distance = data.split("\n")

times_list = [x for x in time.split(" ") if x.isnumeric()]
distances_list = [x for x in distance.split(" ") if x.isnumeric()]

all_races = list(zip(times_list, distances_list))

multiplicator = 1

for race in all_races:
    wins = 0
    for i in range(int(race[0])):
        if i * (int(race[0]) - i) > int(race[1]):
            wins += 1

    multiplicator *= wins

print("solution pt 1:", multiplicator)

total_time = "".join(times_list)
total_distance = "".join(distances_list)

wins = 0
for i in range(int(total_time)):
    if i * (int(total_time) - i) > int(total_distance):
        wins += 1
        
print("solution pt 2:", wins)