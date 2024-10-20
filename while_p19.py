n = int(input())
n_second_digit = 0

while n > 9:
    last_second_digit = n % 10
    n_second_digit = last_second_digit
    n //= 10

print(n_second_digit)
