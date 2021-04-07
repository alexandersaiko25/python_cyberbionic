class Car:

    def __init__(self, brand, model, gas):
        self.brand = brand
        self.model = model
        self.gas = gas

    def __str__(self):
        b = "Название автомобиля: " + self.brand + " " + self.model
        return  b

    def drive(self):
        print("Проехали 1 км...")

    def fuel_consumption(self):
        while self.gas != 0:
            Car.drive(self)
            self.gas -= 1
            if self.gas == 0:
                print("Топливо закончилось")
                Car.add_fuel(self)

    def add_fuel(self):
        ask_refueling = input("Хотите заправить авто(Y/N)? ")
        if ask_refueling == "Y":
            refueling = int(input("На сколько литров дозаправим бак? "))
            self.gas = refueling + self.gas
            Car.fuel_consumption(self)
        elif ask_refueling == "N":
            print("Стойте на обочине. Отдыхайте")
            quit()



car1 = Car("Audi", "A4", 10)
print(car1)
car1.fuel_consumption()
car1.add_fuel()
