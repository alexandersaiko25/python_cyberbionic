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

human = Celsius(40)
print(human.temperature)
print(human.to_fahrenheit())