with open('text.txt', 'w') as file:
    text = input('Введите текст:\n')
    while text:
        file.write(f'{text}\n')
        text = input('Введите текст: \n')




