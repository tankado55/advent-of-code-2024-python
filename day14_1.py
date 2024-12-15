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

for _ in range(100):
    for robot in robots:
        robot.simulate()


q1 = 0
q2 = 0
q3 = 0
q4 = 0
m_x = X_SIZE //2
m_y = Y_SIZE //2

for robot in robots:
    if robot.x == m_x or robot.y == m_y:
        continue
    if robot.y < m_y:
        if robot.x < m_x:
            q1 += 1
        else:
            q2 += 1
    else:
        if robot.x < m_x:
            q4 += 1
        else:
            q3 += 1


print(q1 * q2 * q3 * q4)

# 221142636
