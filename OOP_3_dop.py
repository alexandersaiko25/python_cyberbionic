class MyError(Exception):

    def __init__(self, distance, radius):
        self.distance = distance
        self.radius = radius

    def val_inp(self):
        if 0 < self.distance < self.radius:
            print("all OK")
        elif self.radius < self.distance:
            print("not OK")
        else:
            raise AssertionError("Неверное значение дистанции", self.distance)

distance = int(input("Введите дистанцию: "))
radius = int(input("Введите радиус: "))

obj = MyError(distance, radius)
obj.val_inp()