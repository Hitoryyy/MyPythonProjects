num = int(input())

first_num = num // 100
second_num = (num // 10) % 10
last_num = num % 10

print(
    "Кол-во сотен:",
    first_num,
    "Кол-во десятков:",
    second_num,
    "Кол-во единиц:",
    last_num,
)
