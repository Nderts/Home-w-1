a = input('Введите строку из нескольких слов, разделенных пробелами: ')
b = a.split(' ')
for numb, word in enumerate(b):
    print(f'{numb} - {word[:10]}')

