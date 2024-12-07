import re
import collections

result = 0
f = open("input_7.txt", "r")

def back(calibration, values, start, total):
    if start == len(values):
        if calibration == total:
            return True
        else:
            return False
    
    if back(calibration, values, start + 1, total + values[start]):
        return True
    if back(calibration, values, start + 1, total * values[start] if total != 0 else values[start]):
        return True
    next_total = int(str(total) + str(values[start])) if total != 0 else values[start]
    if back(calibration, values, start + 1, next_total):
        return True
    return False


for line in f:
    calibration = int(line.split(':')[0])
    values = [int(x) for x in line.split(':')[1].split()]

    if back(calibration, values, 0, 0):
        result += calibration

print(result)
    
# 11396 too low
# 2941973819040