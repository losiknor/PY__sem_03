# СЛОВАРЬ
# Структурировать: id, name, date
# Что делать с данными: посмотреть (по id), добавить, удалить
program = True
dictionary = {
    1:{'name1','date1'},
    2:{'name2','date2'},
    3:{'name3','date3'},
    4:{'name4','date4'},
    5:{'name5','date5'}
}

while(program == True):
    print('1. View\n2. Add\n3. Remove\n4. Exit')

    choice = input('\n')

    if choice == '4':
        program = False
        continue

    if choice == '1':
        id = int(input('Input id: '))
        print(f'\n{dictionary[id]}\n')
        # print(f'\n{dictionary[id][0]}\n{dictionary[id][1]}\n') # красиво как-то сделали, но у меня не работает(

    if choice == '2':
        id = int(input('\nInput id: '))
        name = input('\nInput name: ')
        date = input('\nInput date: ')
        dictionary[id] = {name, date}

    if choice == '3':
        id = int(input('Input id: '))
        del dictionary[id]