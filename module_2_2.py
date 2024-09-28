s = input('введите три целых числа через запятую: ')
first,second,third = s.split(sep=',')
first = int(first)
second = int(second)
third = int(third)
if first == second and second == third:
    print(3)
elif first == second or second == third or second == third:
    print(2)
else:
    print(0)