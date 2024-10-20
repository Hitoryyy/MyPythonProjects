n = int(input())
max = 0
min = 9

while n != 0:
    digit = n % 10
    if digit > max:
        max = digit
    if digit < min:
        min = digit
    n //= 10

print('Максимальная цифра равна',max)
print('Минимальная цифра равна',min)