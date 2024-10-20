n = int(input())

f_1 = 1
f_2 = 0


for _ in range(1, n + 1):
   f_n = f_1
   f_1 = f_n + f_2
   f_2 = f_n
   print(f_n, end = ' ')
