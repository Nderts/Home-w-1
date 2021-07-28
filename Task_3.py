def my_func(a, b, c):
    sum = a + b + c
    return sum - min(a, b, c)
a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))
f = my_func(a, b, c)
print(f)