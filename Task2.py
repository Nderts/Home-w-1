userlist = input('Введите список: ')
itog = userlist.split(' ')

for i in range(len(itog) // 2):
    a1, a2 = 2 * i, 2 * i + 1
    itog[a1],   itog[a2] =   itog[a2],   itog[a1]

print(f'Итоговый список: {itog}')