import re
import collections

result = 0
f = open("input_5.txt", "r")

# Parsing
rules = []
updates = []

while f:
    line = f.readline()
    if line == "\n":
        break
    rules.append([int(x) for x in line.replace('\n', '').split('|')])

while f:
    line = f.readline()
    if not line:
        break
    updates.append([int(x) for x in line.replace('\n', '').split(',')])

before_of = collections.defaultdict(list)

for before, after in rules:
    before_of[before].append(after)

def isIllegal(befores, num):
    for before_i in range(len(befores)):
        if befores[before_i] in before_of[num]:
            return before_i
        #if isIllegal(befores, before): return True
    return -1

for update in updates:
    fail = False
    for i in range(1, len(update)):
        illegal_i = isIllegal(update[0:i], update[i])
        while illegal_i != -1:
            update.insert(illegal_i, update[i])
            del update[i + 1]       
            fail = True
            illegal_i = isIllegal(update[0:i], update[i])
    if fail:
        m = len(update) // 2
        print(update[m], update)
        result += update[m]

        



print(result)

# 4957