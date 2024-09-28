my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while 1 > 0:
    if i + 1 > len(my_list):
        break
    a = my_list[i]
    if a < 0:
        break
    if a > 0:
        print(a)
    i = i+1