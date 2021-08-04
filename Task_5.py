import random
with open('nums.txt', 'w') as file:
    for i in range(30):
        file.write(f'{random.randint(0, 10)}')
with open ('nums.txt') as file:
    num_str = file.read().split()
    sum = 0
    for num in num_str:
        sum += int(num)
print(sum)