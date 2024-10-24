n = int(input())
n_c = 1
for i in range(1, n + 1):
    for j in range(i):
       print(n_c, end=' ')
       n_c += 1
    print()
