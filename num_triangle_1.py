n = int(input())
n_c = 0

for i in range(n + 1):
    for j in range(i):
        print(j + 1, end=' ')
        n_c = j
    for k in range(n_c, 0, -1):    
        print(k, end=' ')
    print()
