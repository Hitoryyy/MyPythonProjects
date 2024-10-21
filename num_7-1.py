num = int(input())
n = num

while n != 0:
    last = n % 10
    if last == 7:
        print('YES')
        break
    n //= 10
else:
    print('NO')