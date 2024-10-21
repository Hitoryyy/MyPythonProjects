num = int(input())
number = num
flag = False

while num != 0:
    last_digit = num % 10
    if last_digit == 7:
        flag = True
        break
    num //= 10

if flag:
    print('Число', number, 'содержит цифру 7')
else:
    print('Число', number, 'не содержит цифру 7')