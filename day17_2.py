import re
import collections
import functools
import math
import heapq

result = []
lines = open("input_17.txt", "r").readlines()

A = int(lines[0].split(':')[1])
B = int(lines[1].split(':')[1])
C = int(lines[2].split(':')[1])
ip = 0

program = [int(x) for x in lines[4].split(':')[1].split(',')]

combo = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: A,
    5: B,
    6: C,
    7: 7
}

    
# for i in range(1000000, 1000000000):
#     A = i
#     ip = 0
#     validating_i = 0
#     while ip + 1 < len(program):
#         op = program[ip]
#         operand = program[ip + 1]

#         if op == 0: # division
#             A = int(A / pow(2, combo[operand]))
#         elif op == 1:
#             B = B ^ operand
#         elif op == 2:
#             B = combo[operand] % 8
#         elif op == 3:
#             if A == 0:
#                 pass
#             else:
#                 ip = operand
#                 continue
#         elif op == 4:
#             B = B ^ C
#         elif op == 5:
#             if combo[operand] % 8 != program[validating_i]:
#                 result = ''
#                 break
#             validating_i += 1
#             result += str(combo[operand] % 8) + ","
#             if validating_i > 6:
#                 print(i, result)
#             if validating_i == len(program):
#                 print(i, result)
#                 break
#         elif op == 6:
#             B = int(A / pow(2, combo[operand]))
#         elif op == 7:
#             C = int(A / pow(2, combo[operand]))
#         update_combo()
#         ip += 2

# @functools.cache
def rec(A, B, C, ip):
    global result
    if ip + 1>= len(program):
        return None

    combo = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: A,
        5: B,
        6: C,
        7: 7
    }
    
    op = program[ip]
    operand = program[ip + 1]

    if op == 0: # division
        A = int(A / pow(2, combo[operand]))
    elif op == 1:
        B = B ^ operand
    elif op == 2:
        B = combo[operand] % 8
    elif op == 3:
        if A == 0:
            pass
        else:
            ip = operand
            return rec(A, B, C, ip)
    elif op == 4:
        B = B ^ C
    elif op == 5:
        result.append(combo[operand] % 8)
        return (A, B, C, ip, combo[operand] % 8)
    elif op == 6:
        B = int(A / pow(2, combo[operand]))
    elif op == 7:
        C = int(A / pow(2, combo[operand]))
    ip += 2
    return rec(A, B, C, ip)


start_bin = '0b' + str(pow(10, 45))
#increment = '0b' + str(pow(10, 46))
# i = int(start_bin, 2) | int(increment, 2)
# print("bin: ", start_bin)
# print("bin: ", increment)
# print("bin: ", bin(i))

queue = collections.deque()
queue.append((0, 0))
#queue.append((136889197658112, 4))
#queue.append((136902404017920, 4))
while True:
    start, bit_tris = queue.popleft()
    for k in range(1, 8):
        # i =  start | k << (45 - (bit_tris) * 3)
        i =  start | k << max(0, (45 - (bit_tris) * 3))
        A = i
        B = 0
        C = 0
        ip = 0
        result = []
        while True: # main
            out_tuple = rec(A, B, C, ip)
            if not out_tuple: break
            A, B, C, ip, out = out_tuple
            ip += 2

        control_i = 0
        for j in range(len(result) - 1, -1, -1):
            if result[j] == program[j]:
                control_i += 1
            else:
                break
        if control_i == 16 and i < 109020013201563:
            print(i, bin(i), result, "matched: ", control_i, "k: ", k)
        if control_i > bit_tris and i < 109020013201563:
            queue.append((i, bit_tris + 1))
            queue.append((i, bit_tris + 2))
            queue.append((i, bit_tris + 3))
            queue.append((i, control_i))

    #to_or = '0b' + str(pow(10, 48 - ((control_i + 1) * 3)))
    #i = i | int(to_or, 2)

# 3287450 too low
# 109157464674049 wrong
# 136902404016283 wrong
# 136902404016538 wrong
# 136902404017921
# 136902404017921 too high
# 136902404041114 too high
# 136902413447945
# 136902953406209