city_1 = input()
city_2 = input()
city_3 = input()

length_1 = len(city_1)
length_2 = len(city_2)
length_3 = len(city_3)

length_min = min(length_1, length_2, length_3)
length_max = max(length_1, length_2, length_3)

if length_min == length_1:
    print(city_1)
elif length_min == length_2:
    print(city_2)
elif length_min == length_3:
    print(city_3)

if length_max == length_1:
    print(city_1)
elif length_max == length_2:
    print(city_2)
elif length_max == length_3:
    print(city_3)