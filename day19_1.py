import re
import collections
import functools
import math

result = 0
f = open("input_19_ex.txt", "r")

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
            return True
        else:
            return False
    c = combination[0]
    if c in node.links:
        if find(node.links[c], combination[1:]): return True
    if node.end:
        return find(root, combination)
    else:
        return False

for comb in combinations:
    if find(root, comb): result += 1

print(result)

# 107 too low