class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print("GO")
    def stop(self):
        print("Stop")
    def turn(self, direction):
        print(f"Turned to {derection}")
    def showspeed(self):
        print(f"Car speed is {self.speed}")

class TownCar(Car):
    def showspeed(self):
        super().showspeed()
        if self.speed > 60:
            print("High speed!")
class SportCar(Car):
    pass
class WorkCar(Car):
    def showspeed(self):
        super().showspeed()
        if self.speed > 40:
            print("High speed!")
class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

town = TownCar(110, "White", "Town")
sport = SportCar(180, "Yellow", "Sport")
work = WorkCar(60, "Black", "Work")
police = PoliceCar(90, "Blue", "Police")

town.showspeed()
work.showspeed()







