import re
import collections

result = 0
f = open("input_6.txt", "r")
mat = [[elem for elem in row if elem != '\n'] for row in f]
m = len(mat)
n = len(mat[0])
pos_queue = []

directions = [(-1,-0), (0,1), (1, 0), (0, -1)]
dir_idx = 0
def isOut(i, j):
    if i < 0 or i >= len(mat):
        return True
    if j < 0 or j >= len(mat[0]):
        return True

pos = ()
for i in range(m):
    for j in range(n):
        if mat[i][j] == '^':
            pos = (i, j)
            break
start = pos

def is_loop(obstacle, dir_idx):
    test_mat = [row[:] for row in mat]
    test_mat[obstacle[0]][obstacle[1]] = '#'
    pos = start
    loop_dict = {}
    while True:

        
        next = tuple(map(sum, zip(pos, directions[dir_idx])))
        if isOut(next[0], next[1]):
            return False
        if test_mat[next[0]][next[1]] == '#':
            if loop_dict.get((pos[0], pos[1], dir_idx), False):
                return True
            loop_dict[(pos[0], pos[1], dir_idx)] = True
            dir_idx = (dir_idx + 1) % 4
            continue
            
        test_mat[pos[0]][pos[1]] = 'X'
        pos = next

# Start Algo
test_mat = [row[:] for row in mat]
while True:
    if pos[0] != start[0] or pos[1] != start[1]:
        test_mat[pos[0]][pos[1]] = 'X'

    next = tuple(map(sum, zip(pos, directions[dir_idx])))
    if isOut(next[0], next[1]):
        break
    if mat[next[0]][next[1]] == '#':
        dir_idx = (dir_idx + 1) % 4
        next = tuple(map(sum, zip(pos, directions[dir_idx])))
        if isOut(next[0], next[1]):
            break
    pos = next

for i in range(m):
    for j in range(n):
        if test_mat[i][j] == 'X':
            pos_queue.append((i, j))

for obs in pos_queue:
    if is_loop(obs, dir_idx=0):
        result += 1

print(result)

# 1: 5129

# 2: 1903 too high
# 2: 1902 too high