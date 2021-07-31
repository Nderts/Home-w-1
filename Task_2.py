list = [1, 40, 22, 198, 34, 138, 12, 2, 2, 4, 99, 30, 2]
result = [list[i] for i in range(1, len(list)) if list[i] > list[i-1]]
print(result)


