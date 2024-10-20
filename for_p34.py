largest = int(input())

for _ in range(9):
    num = int(input())
    if num > largest:
        largest = num

print('Наибольшее число равно', largest)