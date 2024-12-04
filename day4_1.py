import re

f = open("input_4.txt", "r")
mat = [[elem for elem in row if elem != '\n'] for row in f]
result = 0

directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]

char_dic = {'X': 0, 'M': 1, 'A': 2, 'S': 3}

def isOut(i, j):
    if i < 0 or i >= len(mat):
        return True
    if j < 0 or j >= len(mat[0]):
        return True

def helper(i, j, dir_i, dir_j):
    global result
    if char_dic[mat[i][j]] == 3:
        result += 1

    if not isOut(i + dir_i, j + dir_j) and char_dic[mat[i][j]] + 1 == char_dic[mat[i + dir_i][j + dir_j]]:
            helper(i + dir_i, j + dir_j, dir_i, dir_j)


for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] == 'X':
            for dir_i, dir_j in directions:
                if not isOut(i + dir_i, j + dir_j) and char_dic[mat[i][j]] + 1 == char_dic[mat[i + dir_i][j + dir_j]]:
                    helper(i, j, dir_i, dir_j)



print(result)

# 2860 too high
# 2551