
f = open("input_1.txt", "r")
my_sum = 0

lefts = []
rights = []

for l in f:
    splitted = l.split()
    lefts.append(int(splitted[0]))
    rights.append(int(splitted[1]))

lefts.sort()
rights.sort()

for i in range(len(lefts)):
    my_sum += abs(rights[i] - lefts[i])

print(my_sum)
print(sum(lefts), sum(rights), sum(rights) - sum(lefts))
