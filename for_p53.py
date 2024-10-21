n = int(input())

counter_1 = 0
counter_2 = 1

for _ in range(1, n + 1):
    n_p = int(input())
    if n_p > counter_1:
        counter_2 = counter_1
        counter_1 = n_p
    elif n_p > counter_2:
        counter_2 = n_p

print(counter_1, counter_2, sep = '\n')