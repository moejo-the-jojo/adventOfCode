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

curr_min = float("inf")

separated_blocks = separated_blocks[1:]

print("here we go6")

# for seeds_range in seeds_list:
#     print("new range")
#     #new_seedlist = list(range(seeds_range[0], seeds_range[0]+seeds_range[1]))
#     for block in separated_blocks:
#         # new_seedlist = []
#         epic_seeds = []
#         block = block.split("\n")[1:]
#         temp_seedlist = new_seedlist.copy()
#         for line in block:
#             end, start, total_range = [int(x) for x in line.split(" ")]
#             difference = end - start
#             for j in new_seedlist:
#                 if j >= start and j < (start + total_range):
#                     epic_seeds.append(int(j + difference))
#                     temp_seedlist.remove(j)
                
#         if len(temp_seedlist) > 0:
#             epic_seeds += temp_seedlist
#         new_seedlist = epic_seeds.copy()
#     if sorted(epic_seeds[0]) < curr_min:
#         curr_min = sorted(epic_seeds[0])



for block in separated_blocks:
    block = block.split("\n")[1:]
    print(block)
    collecting_seeds = []
    ranges_to_go = seeds_list.copy()
    for line in block:
        end, start, total_range = [int(x) for x in line.split(" ")]
        delta = end - start
        for range in ranges_to_go:
            range_start = range[0]
            range_end = range[0] + range[1]
            #complete
            if range_start >= start and range_end <= start + delta:
                collecting_seeds.append([range_start+delta, range_end+delta])
            #partial left
            elif range_start >= start and range_end >= start + delta:
                collecting_seeds.append([range_start+delta, start + delta - range_start + delta])
                ranges_to_go.append([start + delta + 1, range_end - start + delta + 1])
            #partial right
            elif range_start <= start and range_end <= start + delta:
                collecting_seeds.append([start + delta, range_end - start + delta])
                ranges_to_go.append([range_end + 1, start + delta - range_end + 1])
            #partial inner
            elif range_start < start and range_end > start + delta:
                collecting_seeds.append([range_start + delta, range_end + delta])
                ranges_to_go.append([range_start, start - range_start])
                ranges_to_go.append([start + delta + 1, range_end - start + delta + 1])
            else:
                collecting_seeds.append([range_start, range_end])
    seeds_list = collecting_seeds.copy()

print(seeds_list)
print(curr_min)