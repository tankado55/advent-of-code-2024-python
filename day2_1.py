
f = open("input_2.txt", "r")
result = 0

def isSafe(levels):
    direction = 0
    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        if direction == 0:
            direction = diff / abs(diff)
        elif diff / abs(diff) != direction:
            return False
    return True 


for l in f:
    levels = [int(x) for x in l.split()]
    if isSafe(levels):
        result += 1
        continue
    for i in range(len(levels)):
        if isSafe(levels[0:i] + levels[i + 1:]):
            result += 1
            break

print(result)