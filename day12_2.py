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
        return (0, [])
    vis[i][j] = 1
    area = 1
    peri = []

    for next_i, next_j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        if next_i < 0 or next_i >= m: peri.append((i, j, next_i - i, next_j - j)) 
        elif next_j < 0 or next_j >= n: peri.append((i, j, next_i - i, next_j - j)) 
        elif mat[next_i][next_j] != plant: peri.append((i, j, next_i - i, next_j - j)) 
        else:
            measures = measure_dfs(plant, next_i, next_j)
            area += measures[0]
            peri += measures[1]
    return (area, peri)




for i in range(m):
    for j in range(n):
        measures = measure_dfs(mat[i][j], i, j)
        peri = 0
        if measures[0] > 0:
            vec_positions = collections.defaultdict(list)
            for k, l, vec_x, vec_y in measures[1]:
                vec_positions[(vec_x, vec_y)].append((k, l))
            
            plant = mat[i][j]
            # UP scan
            row_scan = sorted(vec_positions[(-1, 0)], key= lambda x: (x[0], x[1]))
            peri += 1
            for scan_i in range(1, len(row_scan)):
                if row_scan[scan_i][0] - row_scan[scan_i - 1][0] != 0 or row_scan[scan_i][1] - row_scan[scan_i - 1][1] > 1:
                    peri += 1
            # DOWN scan
            row_scan = sorted(vec_positions[(1, 0)], key= lambda x: (-x[0], x[1]))
            peri += 1
            for scan_i in range(1, len(row_scan)):
                if row_scan[scan_i][0] - row_scan[scan_i - 1][0] != 0 or row_scan[scan_i][1] - row_scan[scan_i - 1][1] > 1:
                    peri += 1
            # LEFT scan
            col_scan = sorted(vec_positions[(0, -1)], key= lambda x: (x[1], x[0]))
            peri += 1
            for scan_i in range(1, len(col_scan)):
                if col_scan[scan_i][0] - col_scan[scan_i - 1][0] > 1 or col_scan[scan_i][1] - col_scan[scan_i - 1][1] != 0:
                    peri += 1
            # RIGHT scan
            col_scan = sorted(vec_positions[(0, 1)], key= lambda x: (-x[1], x[0]))
            peri += 1
            for scan_i in range(1, len(col_scan)):
                if col_scan[scan_i][0] - col_scan[scan_i - 1][0] > 1 or col_scan[scan_i][1] - col_scan[scan_i - 1][1] != 0:
                    peri += 1

            print(plant, measures[0], peri)
            result += measures[0] * peri

print(result)


# 1070896 too high
# 921636