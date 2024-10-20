n = int(input())
count = 0
lost_digital_1 = n % 10

while n != 0:
    lost_digital_2 = n % 10
    n //= 10
    if lost_digital_1 != lost_digital_2:
        count = 1
    
if count != 0:
    print('NO')
else:
    print('YES')