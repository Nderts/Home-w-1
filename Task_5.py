def final_sum(num, stop):
    list = num.split(' ')
    sum = 0
    for i in list:
        if i == stop:
            break
        sum = sum + int(i)
    return sum

stop = '!'
finish = False
n = 0
while not finish:
    num = input('Введите числа, разделенные пробелом: ')
    n = n + final_sum(num, stop)
    finish = stop in num
    print(f"Сумма = {n}")