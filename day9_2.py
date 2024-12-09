import re
import collections

result = 0
f = open("input_9.txt", "r")
line = list(f.readline().replace('\n', ''))
compacted_data = []
idx = 0
n = len(line)

line_copy = [x for x in line]

def getFit(idx, space):
    idx_r = (n - 1) // 2
    r_left_i = n - 1
    r_left = int(line_copy[r_left_i])
    while r_left == 0 or r_left > space:
        r_left_i -= 2
        r_left = int(line_copy[r_left_i])      
        idx_r -= 1
        if idx_r <= idx or idx_r < 0:
            return (0,0)
    else:
        line_copy[r_left_i] = 0
        return (idx_r, r_left)


for i in range(0, n, 2):
    data_count = int(line[i])
    space_count = int(line[i + 1]) if i + 1 < n else 0
    # regular
    if line_copy[i] != 0:
        for _ in range(data_count):
            compacted_data.append(idx)
    else:
        while data_count > 0:
            to_fit, count = getFit(idx, data_count)
            if count == 0:
                for _ in range(data_count):
                    compacted_data.append(0)
                break
            else:
                for _ in range(count):
                    compacted_data.append(to_fit)
                data_count -= count

    while space_count > 0:
        to_fit, count = getFit(idx, space_count)
        if count == 0:
            for _ in range(space_count):
                compacted_data.append(0)
            break
        else:
            for _ in range(count):
                compacted_data.append(to_fit)
            space_count -= count
    idx += 1

for i, num in enumerate(compacted_data):
    result += num * i    
print(result)

