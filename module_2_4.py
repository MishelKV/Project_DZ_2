numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime=True
for i in numbers:
    if i == 1:
        b = 0
    else:
        b = -1
    for j in numbers:
        c = float(i % j)
        if c == 0:
            b = b + 1
        is_prime = b > 1
    if is_prime == False:
        if i > 1:
            primes.append(numbers[i - 1])
    elif is_prime == True:
        if i > 1:
            not_primes.append(numbers[i - 1])
print(f"Простые числа: {primes}")
print(f"Не простые числа: {not_primes}")
