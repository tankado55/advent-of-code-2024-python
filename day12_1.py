import re
import collections
import functools
import math

result = 0
f = open("input_12.txt", "r")
mat = [[elem for elem in row if elem != '\n'] for row in f]
vis = [[0 for _ in row] for row in mat]

m = len(mat)
n = len(mat[0])

def measure_dfs(plant, i, j):
    if vis[i][j]:
        return (0, 0)
    vis[i][j] = 1
    area = 1
    peri = 0

    for next_i, next_j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        if next_i < 0 or next_i >= m: peri += 1
        elif next_j < 0 or next_j >= n: peri += 1
        elif mat[next_i][next_j] != plant: peri += 1
        else:
            measures = measure_dfs(plant, next_i, next_j)
            area += measures[0]
            peri += measures[1]
    return (area, peri)




for i in range(m):
    for j in range(n):
        measures = measure_dfs(mat[i][j], i, j)
        result += measures[0] * measures[1]

print(result)


