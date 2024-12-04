import re

f = open("input_3.txt", "r")
result = 0

green_light = True
for line in f:
    match = re.search(r'mul\(([0-9]*),([0-9]*)\)', line)
    print(len(line))
    
    while match:
        dont = re.search(r'don\'t\(\)', line[:match.span()[0]])
        do = re.search(r'do\(\)', line[:match.span()[0]])
        if dont and do:
            if dont.span()[0] > do.span()[0]:
                green_light = False
        elif do:
            green_light = True
        elif dont:
            green_light = False

        if green_light:
            group = match.group()
            group = group.replace("mul(", "")
            group = group.replace(")", "")
            group = group.split(",")
            result += int(group[0]) * int(group[1])
        i = match.span()[1]
        line = line[i:]
        match = re.search(r'mul\(([0-9]*),([0-9]*)\)', line)


print(result)

# 82842252 too low
# 89912299 too high
# 87163705 OK