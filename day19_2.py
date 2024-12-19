import re
import collections
import functools
import math

result = 0
f = open("input_19.txt", "r")

towels = f.readline().replace('\n', '').replace(',', '').split()
f.readline()
combinations = [x.replace('\n', '') for x in f.readlines()]
print("max", len(max(combinations, key = lambda x: len(x))))

class Node:
    def __init__(self):
        self.links = {}
        self.end = False
        pass
    

root = Node()

def add_link(node, towel):
    if len(towel) == 0:
        node.end = True
        return
    c = towel[0]
    if c not in node.links:
        next = Node()
        node.links[c] = next
    add_link(node.links[c], towel[1:])

for tow in towels:
    add_link(root, tow)

@functools.cache
def find(node, combination):
    global result
    if len(combination) == 0:
        if node.end:
            #result += 1
            return 1
        else:
            return 0
    c = combination[0]
    count = 0
    if c in node.links:
        count += find(node.links[c], combination[1:])
    if node.end:
        count += find(root, combination)
    return count

find(root, 'r')
for comb in combinations:
    result += find(root, comb)

print(result)

# 107 too low