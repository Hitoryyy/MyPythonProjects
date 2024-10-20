n = float(input())
age = 0
if n <= 2:
    age = n * 10.5
elif n > 2:
    age = 21 + (n - 2) * 4   
print(age)