class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print("Start")
class Pen(Stationery):
    def draw(self):
        print("Drawing with pen")
class Pencil(Stationery):
    def draw(self):
        print("Drawing with pencil")
class Handle(Stationery):
    def draw(self):
        print("Drawing with handle")

pen = Pen("a")
pencil = Pencil("b")
handle = Handle("c")
for i in (pen, pencil, handle):
    i.draw()
