x = int(input())

a = x // 100
b = (x % 100) // 10
c = x % 10

n_min = min(a, b, c)
n_max = max(a, b, c)
n_mid = (a + b + c) - (n_min + n_max)

if n_max - n_min == n_mid:
    print("Число интересное")
else:
    print("Число неинтересное")
