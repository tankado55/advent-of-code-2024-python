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
        arr = []
        for elem in row:
            if elem == '#':
                arr.append('#')
                arr.append('#')
            elif elem == 'O':
                arr.append('[')
                arr.append(']')
            elif elem == '.':
                arr.append('.')
                arr.append('.')
            elif elem == '@':
                arr.append('@')
                arr.append('.')
        warehouse.append(arr)
    else:
        break
while f:
    row = list(f.readline().replace('\n', ''))
    if len(row) > 1:
        moves += row
    else:
        break

m = len(warehouse)
n = len(warehouse[0])

start = None
for i in range(len(warehouse)):
    for j in range(len(warehouse[i])):
        if warehouse[i][j] == '@':
            start = (i, j)
            break

directions = {
    '^': (-1,  0),
    '>': ( 0,  1),
    'v': ( 1,  0),
    '<': ( 0, -1)
}

def check_vertical(i, j, dir_i, dir_j):
    
    if warehouse[i][j] == '[' or warehouse[i][j] == ']':
        if warehouse[i][j] == ']': j -= 1
        next_i = i + dir_i
        next_j = j + dir_j
        # find obstacle
        if warehouse[next_i][next_j] == '#' or warehouse[next_i][next_j + 1] == '#':
            return False
        # try to move
        free_space = True
        if warehouse[next_i][next_j] in [']', '[']: 
            if warehouse[next_i][next_j] == ']':
                free_space &= check_vertical(next_i, next_j, dir_i, dir_j)
        if warehouse[next_i][next_j + 1] in [']', '[']:
            free_space &= check_vertical(next_i, next_j + 1, dir_i, dir_j)
        if free_space:
            return True
    return False

def move_vertical(i, j, dir_i, dir_j):
    
    if warehouse[i][j] == '[' or warehouse[i][j] == ']':
        if warehouse[i][j] == ']': j -= 1
        next_i = i + dir_i
        next_j = j + dir_j
        # find obstacle
        if warehouse[next_i][next_j] == '#' or warehouse[next_i][next_j + 1] == '#':
            return False
        # try to move
        free_space = True
        if warehouse[next_i][next_j] in [']', '[']: 
            if warehouse[next_i][next_j] == ']':
                free_space &= check_vertical(next_i, next_j, dir_i, dir_j)
        if warehouse[next_i][next_j + 1] in [']', '[']:
            free_space &= check_vertical(next_i, next_j + 1, dir_i, dir_j)
        if free_space:
            if warehouse[next_i][next_j] in [']', '[']: 
                if warehouse[next_i][next_j] == ']':
                    move_vertical(next_i, next_j, dir_i, dir_j)
            if warehouse[next_i][next_j + 1] in [']', '[']:
                move_vertical(next_i, next_j + 1, dir_i, dir_j)
            warehouse[next_i][next_j] = '['
            warehouse[next_i][next_j + 1] = ']'
            warehouse[i][j] = '.'
            warehouse[i][j + 1] = '.'
            return True
    return False
    

pos = start
for move in moves:
    dire = directions[move]
    next_i = pos[0] + dire[0]
    next_j = pos[1] + dire[1]

    if (move == '^' or move == 'v') and warehouse[next_i][next_j] != '.' and warehouse[next_i][next_j] != '#':
        if move_vertical(next_i, next_j, dire[0], dire[1]):
            warehouse[pos[0] + dire[0]][pos[1] + dire[1]] = '@'
            warehouse[pos[0]][pos[1]] = '.'
            pos = (pos[0] + dire[0], pos[1] + dire[1])
    else:
        to_move = []
        while next_i > 0 and next_i <= m and next_j > 0 and next_j <= n:
            if warehouse[next_i][next_j] == '#':
                break
            if warehouse[next_i][next_j] == ']' or warehouse[next_i][next_j] == '[':
                to_move.append((next_i, next_j))
            elif warehouse[next_i][next_j] == '.':
                if len(to_move) > 0:
                    while to_move:
                        box = to_move.pop()
                        warehouse[box[0] + dire[0]][box[1] + dire[1]] = warehouse[box[0]][box[1]]

                warehouse[pos[0] + dire[0]][pos[1] + dire[1]] = '@'
                warehouse[pos[0]][pos[1]] = '.'
                pos = (pos[0] + dire[0], pos[1] + dire[1])
                break
            next_i = next_i + dire[0]
            next_j = next_j + dire[1]
        
# result
for i in range(m):
    for j in range(n):
        if warehouse[i][j] == '[':
            result += 100 * i + j

print(result)

# 1469401 too low
# 1471049