# Работа со словарями:
my_dict = {'Anastasiia': 1994, 'Olga': 1969}
print(my_dict)
print(my_dict['Olga'])
print(my_dict.get('Volodia'))
my_dict.update({'Dima': 1970, 'Maxim': 2005})
a = my_dict.pop('Anastasiia')
print(a)
print(my_dict)
# Работа с множествами:
my_set = {6, 2, 3, 3,'Anna', True, 'Anna'}
print(my_set)
my_set.add(6.5)
my_set.add((1,4,6))
my_set.discard(3)
print(my_set)