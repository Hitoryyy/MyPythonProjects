n = int(input())

count_1 = 0
count_2 = 0
last_digital_all = n % 10

while n != 0:
    last_digital_1 = n % 10
    count_1 += 1
    n //= 10

while n != 0:
    last_digital_2 = n % 10
    n //= 10
    if last_digital_2 >= last_digital_all:
        count_2 += 1
        last_digital_all = last_digital_2
    else:
        last_digital_all = last_digital_2
    
    
if count_1 == count_2:
    print("YES")
else:
    print("NO")

print(count_1)
print(count_2)