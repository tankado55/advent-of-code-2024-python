import re
import collections
import functools
import math

class Machine:
    def __init__(self, ax, ay, bx, by, prize_x, prize_y):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.prize_x = prize_x
        self.prize_y = prize_y
        self.x = 0
        self.y = 0
        self.a_tokens = 0
        self.b_tokens = 0
    def push_a(self):
        self.x += self.ax
        self.y += self.ay
        self.a_tokens += 1
    def push_b(self):
        self.x += self.bx
        self.y += self.by
        self.b_tokens += 1
    def revert_a(self):
        self.x -= self.ax
        self.y -= self.ay
        self.a_tokens -= 1
    def revert_b(self):
        self.x -= self.bx
        self.y -= self.by
        self.b_tokens -= 1
    def tokens(self):
        return (self.a_tokens * 3) + (self.b_tokens * 1)


result = 0
f = open("input_13.txt", "r").readlines()
machines = []

for i in range(0, len(f), 4):
    a = [int(x) for x in re.findall(r'\d+', f[i])]
    b = [int(x) for x in re.findall(r'\d+', f[i + 1])]
    prize = [int(x) for x in re.findall(r'\d+', f[i + 2])]
    machines.append(Machine(a[0], a[1], b[0], b[1], prize[0], prize[1]))

for machine in machines:
    while machine.x < machine.prize_x and machine.y < machine.prize_y:
        machine.push_b()
    if machine.x == machine.prize_x and machine.y == machine.prize_y:
        print('b', machine.b_tokens, 'a', machine.a_tokens)
        result += machine.tokens()
        continue
    while machine.b_tokens > 0:
        machine.revert_b()
        while machine.x < machine.prize_x and machine.y < machine.prize_y:
            machine.push_a()
        if machine.x == machine.prize_x and machine.y == machine.prize_y:
            result += machine.tokens()
            break


print(result)

# 37680
