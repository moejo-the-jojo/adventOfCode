data = open("2015\inputs\day2.txt", "r").read()

single_packages = data.split("\r")[0].split("\n")[:-1]

total_paper = 0

for package in single_packages:
    l, w, h = package.split("x")
    sides = [int(l)*int(w), int(l)*int(h), int(w)*int(h)]
    total_paper += sum(sides)*2
    total_paper += min(sides)

print("part 1 solution: " + str(total_paper))


total_ribbon = 0

for package in single_packages:
    l, w, h = package.split("x")
    lengths = sorted([int(l), int(w), int(h)])
    total_ribbon += (lengths[0] * 2 + lengths[1] * 2 + lengths[0] * lengths[1] * lengths[2])

print("part 2 solution: " + str(total_ribbon))