import re
import collections
import functools
import math

result = 0
f = open("input_15.txt", "r")

warehouse = []
moves = []
while f:
    row = list(f.readline().replace('\n', ''))
    if len(row) > 1:
        warehouse.append(row)
    else:
        break
while f:
    row = list(f.readline().replace('\n', ''))
    if len(row) > 1:
        moves += row
    else:
        break


