import re
import collections
import functools
import math
import heapq

result = 0
f = open("input_16.txt", "r")
mat = [[elem for elem in row if elem != '\n'] for row in f]
min_cost = collections.defaultdict(lambda: float('inf'))
dir_mat = [[[] for _ in row] for row in mat]

start = None
end = None
m = len(mat)
n = len(mat[0])

for i in range(m):
    for j in range(n):
        if mat[i][j] == 'S':
            start = (i, j)

queue = []


queue.append((0, start[0], start[1], 0, 1, []))

result = 0
final_cost = float('inf')
while queue:
    cost, i, j, dir_i, dir_j, list_so_far = heapq.heappop(queue)
    if ((dir_i, dir_j) not in dir_mat[i][j]):
        dir_mat[i][j].append((dir_i, dir_j))
    
    if mat[i][j] == 'E' and cost <= final_cost:
        final_cost = cost
        end = (i, j)
        print(cost)
        for elem in list_so_far:
            mat[elem[0]][elem[1]] = 'O'
        continue

    #mat[i][j] = '*'
    next_i = i + dir_i
    next_j = j + dir_j
    next_list = list_so_far + [(i, j)]
    if mat[next_i][next_j] != '#' and cost + 1 <= min_cost[(next_i, next_j, dir_i, dir_j)]:
        min_cost[(next_i, next_j, dir_i, dir_j)] = cost + 1
        heapq.heappush(queue, (cost + 1, next_i, next_j, dir_i, dir_j, next_list))
    next_i = i + dir_j
    next_j = j + dir_i
    if mat[next_i][next_j] != '#' and cost + 1001 <= min_cost[(next_i, next_j, dir_j, dir_i)]:
        min_cost[(next_i, next_j, dir_j, dir_i)] = cost + 1001
        heapq.heappush(queue, (cost + 1001, next_i, next_j, dir_j, dir_i, next_list))
    next_i = i - dir_j
    next_j = j - dir_i
    if mat[next_i][next_j] != '#' and cost + 1001 <= min_cost[(next_i, next_j, -dir_j, -dir_i)]:
        min_cost[(next_i, next_j, -dir_j, -dir_i)] = cost + 1001
        heapq.heappush(queue, (cost + 1001, next_i, next_j, -dir_j, -dir_i, next_list))

for i in range(m):
    for j in range(n):
        if mat[i][j] == 'O': result += 1
print(result + 1)

# 2047 too high
# 929 too high
# 559