from math import log

n = int(input())
total = 0
count = 1

for _ in range(n):
    total += 1 / count
    count += 1

total -= log(n)

print(total)
