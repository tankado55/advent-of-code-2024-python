import re
import collections
import functools

result = 0
f = open("input_10.txt", "r")
mat = [[int(elem) for elem in row if elem != '\n'] for row in f]

def dfs(i, j):
    global vis
    if mat[i][j] == 9:
        if vis[i][j] == 0:
            vis[i][j] = 1
            return 1
        return 0

    score = 0
    for next_i, next_j in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
        if next_i >= 0 and next_i < len(mat) and next_j >=0 and next_j < len(mat[0]):
            if mat[next_i][next_j] - mat[i][j] == 1:
                    if vis[next_i][next_j] == 0:
                        vis[next_i][next_j] == 1
                        score += dfs(next_i, next_j)

    return score

vis = [[0 for x in row] for row in mat]
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] == 0:
            vis = [[0 for x in row] for row in mat]
            result += dfs(i, j) 



            
print(result)

