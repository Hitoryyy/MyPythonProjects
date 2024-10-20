n = int(input())
total = 0

while n > 0 and n <= 5:
    if n == 5:
        total += 1
    n = int(input())
    
print(total)