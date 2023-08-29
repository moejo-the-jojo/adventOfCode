import hashlib

data = open("2015/inputs/day4.txt", "r").read()

i = 1

while True:
    result = hashlib.md5((data + str(i)).encode()).hexdigest()
    if str(result)[0:5] == "00000":
        break
    else:
        i += 1

print("part 1 solution: " + str(i))

i = 1

while True:
    result = hashlib.md5((data + str(i)).encode()).hexdigest()
    if str(result)[0:6] == "000000":
        break
    else:
        i+= 1

print("part 2 solution: " + str(i))