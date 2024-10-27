my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
score = 0
while  score < len(my_list):
    number = int(my_list[score])
    score = score + 1
    if number < 0:
        break
    if number == 0:
        continue
    else:
        print(number)