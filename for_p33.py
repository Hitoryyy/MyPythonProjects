largest = 0
for _ in range(10):
    num = int(input())
    if num > largest:
        largest = num

print('Наибольшее число', largest)