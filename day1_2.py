import collections

f = open("input_1.txt", "r")
my_sum = 0

lefts = []
rights = []

dic = collections.defaultdict(int)

for l in f:
    splitted = l.split()
    lefts.append(int(splitted[0]))
    rights.append(int(splitted[1]))

for n in rights:
    dic[n] += 1

for n in lefts:
    my_sum += n * dic[n]

print(my_sum)
