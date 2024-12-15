import re
import collections
import functools
import math

X_SIZE = 101
Y_SIZE = 103

class Robot:
    def __init__(self, x, y, vel_x, vel_y):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        pass

    def simulate(self):
        self.x = (self.x + self.vel_x) % X_SIZE
        self.y = (self.y + self.vel_y) % Y_SIZE

result = 0
lines = open("input_14.txt", "r").readlines()

robots = []
for line in lines:
    data = [int(x) for x in re.findall(r'-?\d+\.?\d*', line)]
    robots.append(Robot(data[0], data[1], data[2], data[3]))

for i in range(10000):
    mat = [[0] * X_SIZE for _ in range(Y_SIZE)]
    for robot in robots:
        robot.simulate()

    for robot in robots:
        mat[robot.y][robot.x] += 1

    f = open("mat.txt", "a")
    for row in mat:
        f.write(''.join(str(x) if x != 0 else '.' for x in row))
        f.write('\n')
    f.write('\n')
    f.write(str(i))
    f.write('\n')
    f.close()
print("ok")
