n = int(input())
lost_digit = n % 10
count = 0

while n != 0:
    lost_digit_while = n % 10
    n //= 10
    if lost_digit_while < lost_digit:
        count = 1

    lost_digit = lost_digit_while

if count != 0:
    print('NO')
else:
    print('YES') 
