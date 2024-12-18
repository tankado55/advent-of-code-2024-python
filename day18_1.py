import re
import collections
import functools
import math
import heapq

result = 0
lines = open("input_18.txt", "r").readlines()
N = 71
I = 2988
mat = [['.' for _ in range(N)] for _ in range(N)]
vis = [[0 for _ in row] for row in mat]

falling = [[int(x) for x in line.replace('\n', '').split(',')] for line in lines]

for i in range(I):
    x = falling[i][0]
    y = falling[i][1]
    mat[y][x] = '#'

queue = collections.deque()
queue.append((0, 0, 0))
vis[0][0] = 1

while queue:
    cost, x, y = queue.popleft()
    if x == N - 1 and y == N - 1:
        print(cost)
        break
    for dir_y, dir_x in [(0,1), (0, -1), (1, 0), (-1, 0)]:
        next_x = x + dir_x
        next_y = y + dir_y
        if next_x >= 0 and next_x < N and next_y >= 0 and next_y < N and vis[next_y][next_x] == 0 and mat[next_y][next_x] != '#':
            vis[next_y][next_x] = 1
            queue.append((cost + 1, next_x, next_y))



print(result)

# 11, 12 no