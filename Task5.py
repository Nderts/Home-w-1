list = [9, 8, 7, 7, 7, 5, 5, 3, 2, 2, 2, 2, 1]
a = int(input('Введите число: '))
inserted = False
for num, elem in enumerate(list):
    if a > elem:
        list.insert(num, a)
        inserted = True
        break

if not inserted:
    list.append(a)

print(list)
