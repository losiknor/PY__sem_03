# списки + list() ---> my_list = [....]
# кортежи + tuple() ---> my_tuple = (....)
# словари: keys(), values(), items() ---> my_dict = {....}
# множества + set() ---> уникальность элементов ---> my_set = {....}
# работа с файлами
# функции

my_list = [1, 2, 3, 4, 5] # список
my_tuple = (1, 2, 3, 4, 5) # кортеж ---> ИСПОЛЬЗУЮТСЯ В СЛОВАРЯХ В КАЧЕСТВЕ КЛЮЧЕЙ!
my_dict = {
    ('Красный', 'Спелый'): 'Помидор',
    1: 'Ещё раз список!'
}
print(my_dict[('Красный', 'Спелый')])
my_dict['new_key_'] = 123
print(my_dict)

my_dict['old_key'] = 123
print(my_dict)
my_dict['new_key'] = 123
print(my_dict)
del my_dict['old_key']
print(my_dict)

my_dict1 = {
    62234: {
        'name': 'Стул',
        'count': 100
    },
    54324: {
        'name': 'Диван',
        'count': 50
    }
}
print(my_dict1[54324]['name'])

for key in my_dict1.keys():
    print(key)
    print(my_dict1[key])

for value in my_dict1.values():
    print(value)
   
for key, value in my_dict1.items():
    print(key, value)

my_set = {1, 2, 3, 4}
my_set.add(5)
print(my_set)