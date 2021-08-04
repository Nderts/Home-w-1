list = {
    'One': "Один",
    'Two': "Два",
    'Three': "Три",
    'Four': "Четыре"
}
with open('text.txt') as file, open('new.txt', 'w') as new_file:
    lines = file.readlines()
    for line in lines:
        data = line.split()
        ru = list.get(data[0])
        new_file.write(f'{line.replace(data[0], ru)}')