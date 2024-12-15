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
    def push_a(self, times):
        self.x += self.ax * times
        self.y += self.ay * times
        self.a_tokens += times
    def push_b(self, times):
        self.x += self.bx * times
        self.y += self.by * times
        self.b_tokens += times
    def revert_a(self):
        to_x = (self.x - self.prize_x) // self.bx
        to_y = (self.y - self.prize_y) // self.by
        times = max(to_x, to_y)
        self.x -= times * self.ax
        self.y -= times * self.ay
        self.a_tokens -= times
    def revert_b(self):
        to_x = math.ceil((self.x - self.prize_x) / self.bx)
        to_y = math.ceil((self.y - self.prize_y) / self.by)
        times = max(to_x, to_y)
        self.x -= times * self.bx
        self.y -= times * self.by
        self.b_tokens -= times
    def tokens(self):
        return (self.a_tokens * 3) + (self.b_tokens * 1)


result = 0
f = open("input_13.txt", "r").readlines()
machines = []

for i in range(0, len(f), 4):
    a = [int(x) for x in re.findall(r'\d+', f[i])]
    b = [int(x) for x in re.findall(r'\d+', f[i + 1])]
    prize = [int(x) for x in re.findall(r'\d+', f[i + 2])]
    machines.append(Machine(a[0], a[1], b[0], b[1], prize[0] + 10000000000000, prize[1] + 10000000000000))

for machine in machines:
    b_times = min(machine.prize_x // machine.bx, machine.prize_y // machine.by)
    machine.push_b(b_times)
    if machine.x == machine.prize_x and machine.y == machine.prize_y:
        print('b', machine.b_tokens, 'a', machine.a_tokens)
        result += machine.tokens()
        continue
    while machine.b_tokens > 0:
        a_to_x = math.ceil((machine.prize_x - machine.x) / machine.ax)
        a_to_y = math.ceil((machine.prize_y - machine.y) / machine.ay)
        a_times = max(a_to_x, a_to_y)
        machine.push_a(a_times)
        machine.revert_b()
        if machine.x == machine.prize_x and machine.y == machine.prize_y:
            result += machine.tokens()
            break


print(result)


# 37680 P1
# 87550094242995