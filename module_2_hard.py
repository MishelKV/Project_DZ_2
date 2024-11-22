result = []
insert1 = int(input("Введите число от 3 до 20 "))
numbers1 = 1
while numbers1 < insert1:
    numbers2 = numbers1+1
    while numbers2 < insert1:
        if insert1 % (numbers1+numbers2) == 0:
            result.append(numbers1)
            result.append(numbers2)
        numbers2 += 1
    numbers1 += 1

result0= ' '
for i in result:
    result0 = result0 + str(i)
result = result0
print(result)