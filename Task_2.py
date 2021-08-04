with open('text.txt') as file:
    text = file.readlines()
    for num, line in enumerate(text):
        count = len(line.split())
        print(f'{num + 1} - {count} слов')