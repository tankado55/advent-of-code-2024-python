import re

f = open("input_4.txt", "r")
mat = [[elem for elem in row if elem != '\n'] for row in f]
result = 0

directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

char_dic = {'X': 0, 'M': 1, 'A': 2, 'S': 3}

def isOut(i, j):
    if i < 0 or i >= len(mat):
        return True
    if j < 0 or j >= len(mat[0]):
        return True

for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] == 'A':
            if not isOut(i + 1,j + 1) and not isOut(i - 1,j - 1) and not isOut(i - 1,j + 1) and not isOut(i + 1,j - 1):
                if (mat[i + 1][j + 1] == 'M' and mat[i - 1][j - 1] == 'S') or (mat[i + 1][j + 1] == 'S' and mat[i - 1][j - 1] == 'M'):
                    if (mat[i - 1][j + 1] == 'M' and mat[i + 1][j - 1] == 'S') or (mat[i - 1][j + 1] == 'S' and mat[i + 1][j - 1] == 'M'):
                        result += 1


print(result)

# 1985