with open('text.txt') as file:
    lines = file.readlines()
    people = {}
    money = 0
    for line in lines:
        inform = line.split()
        new = ({inform[0]: float(inform[1])})
        money += float(inform[1])
summ = money / len(people)
print (f'Средняя = {summ}')
for a, b in people.items():
    if b > summ:
        print(f'{a}: {b}')
