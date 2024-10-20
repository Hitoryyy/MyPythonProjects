n = int(input())
n_sum = 0
n_num = 0
n_mul = 1
n_one_num_1 = n 

while n != 0:
    digit_last = n % 10
    n_sum += digit_last
    n_num += 1
    n_mul *= digit_last
    n //= 10

n_mid = n_sum / n_num
n_one_num = (n_one_num_1 % (10**n_num)) // 10**(n_num - 1)
n_one_d_sum_last_d = (n_one_num_1 % 10) + n_one_num

print(n_sum)
print(n_num)
print(n_mul)
print(n_mid)
print(n_one_num)
print(n_one_d_sum_last_d)
