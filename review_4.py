num = int(input())
flag = True

for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        flag = False
        break

if num > 1 and flag == True:
    print('Число простое')
else:
    print('Число составное')