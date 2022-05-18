# открытие в режиме записи ---> если файла нет, создаёт его! перезаписывает!
my_txt = open('test.txt', 'w')
my_txt.write('Hello, World!')
my_txt.close()

# открытие в режиме чтения
my_txt = open('test.txt', 'r')
print(my_txt.read())
my_txt.close()

# читать и записывать
my_txt = open('test.txt', 'r+')
print(my_txt.write('123\n'))
my_txt.close()

# записывать в конец
my_txt = open('test.txt', 'a+')
print(my_txt.write('123\n'))
my_txt.close()

# 'b+' есть ещё - байтовый режим