def gen_factorial(a):
    x = 1
    for i in range(1, a + 1):
        x *= i
        yield x

a = 20
for p, q in enumerate(gen_factorial(a)):
    print(f"#{p +1} {q}")
