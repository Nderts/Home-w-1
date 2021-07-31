from functools import reduce
list = [i for i in range(100, 1000) if i % 2 == 0]
print(reduce(lambda a, b: a * b, list))