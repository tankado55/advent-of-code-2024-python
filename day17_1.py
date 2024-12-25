import re
import collections
import functools
import math
import heapq

result = ""
lines = open("input_17.txt", "r").readlines()

A = int(lines[0].split(':')[1])
B = int(lines[1].split(':')[1])
C = int(lines[2].split(':')[1])

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

def update_combo():
    combo[4] = A
    combo[5] = B
    combo[6] = C
    

ip = 0
while ip + 1 < len(program):
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
            continue
    elif op == 4:
        B = B ^ C
    elif op == 5:
        result += str(combo[operand] % 8) + ","
    elif op == 6:
        B = int(A / pow(2, combo[operand]))
    elif op == 7:
        C = int(A / pow(2, combo[operand]))
    update_combo()
    ip += 2

print(result)