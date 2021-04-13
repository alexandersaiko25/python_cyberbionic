class Transport:

    def wheels(self):
        print("Есть 4 колеса")

    def body(self):
        print("Есть кузов")

    def bumper(self):
        print("Есть 2 бампера")

    def engine(self):
        print("Есть двигатель")

class Car(Transport):

    def volume_interior(self):
        print("Вместимость до 4х человек")

class FreightСar(Transport):

    def carrying_capacity(self):
        print("Грузоподъёмность свыше 3.5 тонн")

print("Первый объект")
obj = Car()
obj.wheels()
obj.volume_interior()

print("Второй объект")
obj2 = FreightСar()
obj2.engine()
obj2.carrying_capacity()