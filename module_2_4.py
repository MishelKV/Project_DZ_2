numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    is_prime = True
    if i < 2:
        continue
    for j in range(2, i):
        if float(i % j) == 0:
            is_prime = False
            break
    if not (is_prime):
        not_primes.append(i)
    else:
        primes.append(i)

print(f"Простые числа: {primes}")
print(f"Не простые числа: {not_primes}")
