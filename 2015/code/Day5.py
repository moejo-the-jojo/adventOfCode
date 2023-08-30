import re

data = open("2015/inputs/day5.txt", "r").read()

single_words = data.split("\n")

good_count = 0

for word in single_words:
    if len(re.findall(r"[aeiou]", word)) < 3:
        continue
    elif len(re.findall(r"(.)\1", word)) < 1:
        continue
    elif len(re.findall(r"ab|cd|pq|xy", word)) > 0:
        continue
    else:
        good_count += 1

print("part 1 solution: " + str(good_count))


good_count = 0

for word in single_words:
    if len(re.findall(r"(.).\1", word)) < 1:
        continue
    elif len(re.findall(r"(.{2}).*\1", word)) < 1:
        continue
    else:
        good_count += 1

print("part 2 solution: " + str(good_count))