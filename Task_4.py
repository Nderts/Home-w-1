def my_func(x, n):
    if x < 0:
        return 'x должен быть больше 0'
    if n > 0:
        return 'y должен быть меньше 0'
    a = 1
    for i in range(n * -1):
        a *= x
    return 1 / a

x = int(input("введите положительное число x: "))
n = int(input("введите отрицательное число n: "))
print(my_func(x, n))