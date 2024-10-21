num = int(input())
flag = True

for i in range(2, num):
    if num % 2 == 0:
        flag = False
        break

if flag:
    print("Число простое")
else:
    print("Число составное")
