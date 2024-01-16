data = open("2023\inputs\day5.txt", "r").read()
sample_data = """seeds:
79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

seperated_blocks = data.split("\n\n")

seeds_list = seperated_blocks[0].split("\n")[1].split(" ")
seeds_list = [int(x) for x in seeds_list]

seperated_blocks = seperated_blocks[1:]

for block in seperated_blocks:
    new_seedlist = []
    block = block.split("\n")[1:]
    temp_seedlist = seeds_list.copy()
    for line in block:
        end, start, total_range = [int(x) for x in line.split(" ")]
        difference = end - start
        for seed in seeds_list:
            if seed >= start and seed < (start + total_range):
                new_seedlist.append(int(seed + difference))
                temp_seedlist.remove(seed)
            
    if len(temp_seedlist) > 0:
        new_seedlist += temp_seedlist
    seeds_list = new_seedlist.copy()
        
    

print("Solution pt 1:", sorted(seeds_list)[0])

data = open("2023\inputs\day5.txt", "r").read()

separated_blocks = data.split("\n\n")

seeds_list = separated_blocks[0].split("\n")[1].split(" ")
seeds_list = [int(x) for x in seeds_list]
total_seeds_list = []
temp_couple = []
for i in range(len(seeds_list)):
    if i%2 == 0 or i == 0:
        temp_couple.append(seeds_list[i])
    else:
        temp_couple.append(seeds_list[i])
        total_seeds_list.append(temp_couple)
        temp_couple = []

seeds_list = total_seeds_list.copy()

separated_blocks = separated_blocks[1:]


for block in separated_blocks:
    block = block.split("\n")[1:]
    collecting_seeds = []
    ranges_to_go = seeds_list.copy()
    next_line_ranges = []
    for line in block:
        trans_goal, trans_start, trans_range = [int(x) for x in line.split(" ")]
        delta = trans_goal- trans_start
        trans_end = trans_start + trans_range -1
        while len(ranges_to_go) > 0:
            current_range = ranges_to_go.pop(0)
        # for range in ranges_to_go:
            # print(range)
            range_start = current_range[0]
            range_end = current_range[0] + current_range[1] - 1
            #complete
            if trans_start <= range_start and range_end <= trans_end:
                collecting_seeds.append([range_start+delta, current_range[1]])
            #partial left
            elif range_start > trans_start and range_start <= trans_end and range_end > trans_end:
                collecting_seeds.append([range_start+delta, trans_end - range_start + 1])
                ranges_to_go.append([trans_end + 1, range_end - trans_end])
            #partial right
            elif range_end >= trans_start and range_end < trans_end and range_start < trans_start:
                collecting_seeds.append([trans_start + delta, range_end - trans_start])
                ranges_to_go.append([range_start, trans_start - 1 - range_start])
            #partial inner
            elif range_start < trans_start and range_end > trans_end:
                collecting_seeds.append([trans_start + delta, trans_end-trans_start])
                ranges_to_go.append([range_start, trans_start - 1 - range_start])
                ranges_to_go.append([trans_end + 1, range_end - trans_end])
            else:
                next_line_ranges.append([range_start, current_range[1]])
        ranges_to_go += next_line_ranges.copy()
        next_line_ranges = []
    if len(collecting_seeds) == 0:
        pass
    else:
        seeds_list = collecting_seeds.copy() + ranges_to_go.copy()

print("solution pt 2:", sorted(seeds_list, key=lambda x: x[0])[0][0])