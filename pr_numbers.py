a = int(input())
b = int(input())

count = 2

for i in range(a, b + 1):
    count_digit = 0
    digit = 0
    if i == 1:
        continue
    for j in range(1, i + 1):
        digit = i % j
        if digit == 0:
            count_digit += 1
    if count_digit <= count:
        print(i)