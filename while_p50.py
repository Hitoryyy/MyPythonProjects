n = int(input())
lost_digital = n % 10
count = 0

while n != 0:
    lost_digital_while = n % 10
    n //= 10
    if lost_digital != lost_digital_while:
        count = 1

if count != 0:
    print("NO")
else:
    print("YES")
