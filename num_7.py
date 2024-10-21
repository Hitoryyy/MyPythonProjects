num = int(input())
n = num
flag = False

while n != 0:
    last = n % 10
    if last == 7:
        flag = True
        break
    n //= 10

if flag:
    print('YES')
else:
    print('NO')