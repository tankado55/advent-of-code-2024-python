import re
import collections

result = 0
f = open("input_9.txt", "r")
line = list(f.readline())
compacted_data = []
idx = 0
n = len(line)

idx_r = (n - 1) // 2
r_left_i = n - 2
r_left = int(line[r_left_i])
def getLast():
    global r_left
    global r_left_i
    global idx_r
    if r_left > 0:
        r_left -= 1
        return idx_r
    else:
        idx_r -= 1
        r_left_i -= 2
        r_left = int(line[r_left_i]) - 1
        return idx_r


for i in range(0, n, 2):
    data_count = int(line[i])
    space_count = int(line[i + 1]) if i + 1 < n else 0
    if i >= r_left_i:
        for _ in range(r_left):
            compacted_data.append(idx)
        break
    for _ in range(data_count):
        compacted_data.append(idx)
    idx += 1
    for _ in range(space_count):
        compacted_data.append(getLast())

for i, num in enumerate(compacted_data):
    result += num * i






            
print(result)

