class Celsius:

    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Принимает значение ... ")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Устанавливаем значение...")
        if value < -273.15:
            raise ValueError("Температура ниже -273 градуса невозможна")
        self._temperature = value

class Fahrenheit:

    def __init__(self, temperature = -17):
        self.temperature = temperature

    def __str__(self):
        return f'({self.temperature})'

    def to_celsius(self):
        return (self.temperature - 32) * 5/9

    @property
    def temperature(self):
        print("Принимает значение ... ")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Устанавливаем значение...")
        if value < -459.67:
            raise ValueError("Температура ниже -459.67 градуса невозможна")
        self._temperature = value


converter = input("Какие единицы будете вводить (C/F) ?")
zn = int(input("Введите значение в градусах Цельсия либо Фаренгейта: "))

if converter == "c" or converter == "C":
    human = Celsius(zn)
    print(human.temperature)
    print(human.to_fahrenheit())

elif converter == "f" or converter == "F":
    human = Fahrenheit(zn)
    print(human.temperature)
    print(human.to_celsius())
