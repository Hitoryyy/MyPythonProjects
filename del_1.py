n1 = int(input())
n2 = int(input())
final_digit = 0
final_total = 0

for i in range(n1, n2 + 1):
    total = 0
    for j in range(1, i + 1):
        if i % j == 0:
            total += j
            digit = i
            if total >= final_total:
                final_digit = digit
                final_total = total

print(final_digit, final_total)                
