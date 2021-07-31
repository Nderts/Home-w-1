from itertools import cycle, count
a = 100
list = [i for i in range(5)]
x = count()
y = cycle(list)
print([next(x) for i in range(a)])
print([next(y) for i in range(a)])

