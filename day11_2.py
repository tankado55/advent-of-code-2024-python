import re
import collections
import functools
import math

result = 0
f = open("input_11.txt", "r")
stones = [int(x) for x in f.readline().split()]

@functools.cache
def compute(n, stone):
    #0  0
    #1  1
    #2  2024
    #3  20 24
    #4  2 0 2 4
    #5  4048 1 4048 8096
    #6  4 0 4 8 2024 4 0 4 8 8 0 9 6
    #7  8096 1 8096 16192 20 24 8096 1 8096 16192 16192 1 18216 12144

    if n == 0 and stone > 9 and int((math.log(stone, 10) + 1)) % 2 == 0: return 2
    if n == 0: return 1
    
    if stone == 0:
            return compute(n - 1, 1)
    if stone > 9 and int((math.log(stone, 10) + 1)) % 2 == 0:
        m = len(str(stone)) // 2
        return  compute(n - 1, int(str(stone)[:m])) + compute(n - 1, int(str(stone)[m:]))
    return compute(n - 1, stone * 2024)


for stone in stones:
    result += compute(74, stone)


            
print(result)

# 272673043447232 too high
# 414155049637777
# 179517062814601 too low
# 272673043446478
