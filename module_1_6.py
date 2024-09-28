my_dict = {'Kosta':1969, 'Nata':1968, 'Alex':1997}
print(my_dict)
print(my_dict['Kosta'])
my_dict['Luda'] = 1973
print(my_dict)
my_dict.update({'Zoya':1949,
                'lada':1993})
print(my_dict)
a = my_dict.pop('Kosta')
print(my_dict)
print(a)
print(my_dict.items())
my_set = {8,'duck',3.5,8,'duck', 3}
print(my_set)
my_set = {8,'duck',3.5,8,'duck', 3}
my_set.update({5,'s'})
print(my_set)
my_set.discard(2)
my_set.remove(8)
print(my_set)