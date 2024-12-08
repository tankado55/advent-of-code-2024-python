import re
import collections

def isOut(i, j):
    if i < 0 or i >= len(mat):
        return True
    if j < 0 or j >= len(mat[0]):
        return True

f = open("input_8.txt", "r")
result = 0

mat = [[elem for elem in row if elem != '\n'] for row in f]
d_mat = [[x for x in row] for row in mat]
m = len(mat)
n = len(mat[0])

positions = collections.defaultdict(list)
for i in  range(m):
    for j in range(n):
        if mat[i][j] != '.':
            positions[mat[i][j]].append((i, j)) 


for freq in positions.keys():
    freq_len = len(positions[freq])
    for i in range(freq_len):
        for j in range(i + 1, freq_len):
            freq_positions = positions[freq]
            vec_x = freq_positions[j][0] - freq_positions[i][0]
            vec_y = freq_positions[j][1] - freq_positions[i][1]
            vec_offset = 0
            anti1 = (freq_positions[j][0] + (vec_x * vec_offset), freq_positions[j][1] + (vec_y * vec_offset))
            while not isOut(anti1[0], anti1[1]):
                if d_mat[anti1[0]][anti1[1]] != '#':
                    result += 1
                d_mat[anti1[0]][anti1[1]] = '#'
                vec_offset += 1
                anti1 = (freq_positions[j][0] + (vec_x * vec_offset), freq_positions[j][1] + (vec_y * vec_offset))
            
            vec_offset = 0
            anti2 = (freq_positions[i][0] - (vec_x * vec_offset), freq_positions[i][1] - (vec_y * vec_offset))
            while not isOut(anti2[0], anti2[1]):
                if d_mat[anti2[0]][anti2[1]] != '#':
                    result += 1
                d_mat[anti2[0]][anti2[1]] = '#'
                vec_offset += 1
                anti2 = (freq_positions[j][0] - (vec_x * vec_offset), freq_positions[j][1] - (vec_y * vec_offset))

            
print(result)

