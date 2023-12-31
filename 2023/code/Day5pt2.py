data = open("2023\inputs\day5.txt", "r").read()


seperated_blocks = data.split("\n\n")

seeds_list = seperated_blocks[0].split("\n")[1].split(" ")
seeds_list = [int(x) for x in seeds_list]
total_seeds_list = []
for i in range(len(seeds_list)):
    if i%2 == 0:
        temp_start = seeds_list[i]
    else:
        for j in range(temp_start, temp_start + seeds_list[i]):
            total_seeds_list.append(j)

seeds_list = total_seeds_list.copy()
print(seeds_list)

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
        
    

print(sorted(seeds_list))