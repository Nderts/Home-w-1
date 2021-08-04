result = {}
with open('text.txt') as file:
    lines = file.readlines()
    for line in lines:
        data = line.split()
        hr = 0
        for elem in data[1:]:
            if elem != '-':
                num = '0'
                for i in elem:
                    if i.isdigit():
                        num += i
                    else:
                        break
                hr += int(num)
        result.update({data[0].strip(':'): hr})
print(result)