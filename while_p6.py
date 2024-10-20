str = input()
total = 0

while str != 'стоп' and str != 'хватит' and str != 'достаточно':
    str = input()
    total += 1
    
print(total)