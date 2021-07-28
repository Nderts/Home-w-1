def func(a):
    word = a[0]. upper() + a[1:].lower()
    return word
lane = input("Введите слова, разделенные пробелом: ")
for word in lane.split(' '):
    print(f'{func(word)} ', end='')
