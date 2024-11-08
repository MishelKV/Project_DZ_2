result = []
insert1 = int(input("Введите число от 3 до 20 "))
numbers1 = 0
while numbers1 < 21:
    numbers1+=1
    numbers2 = 1
    while numbers2 < 21:
        if insert1 % (numbers1+numbers2) == 0 and numbers1<numbers2:
            result.append(numbers1)
            result.append(numbers2)
        numbers2 += 1
result0= ' '
for i in result:
    result0 = result0 + str(i)
result = result0
print(result)