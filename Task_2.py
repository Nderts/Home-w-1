class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def weight(self, grav, thick):
        return self._length * self._width * grav * thick / 1000

n = Road(3000, 50)
print(n.weight(30, 10))