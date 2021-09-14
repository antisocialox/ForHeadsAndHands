from random import randint

n = int(input())
array = [[] for i in range(n)]
lens = []
for i in range(n):
    length = randint(1, 10000)
    while length in lens:
        length = randint(1, 10000)
    for j in range(length):
        array[i].append(randint(-10000, 10000))
    array[i].sort(reverse=(i % 2 == 0))
    lens.append(length)