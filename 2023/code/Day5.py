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
        
    

print("Solution pt 1: " + str(sorted(seeds_list)))

