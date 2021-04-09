import random

class Warrior:

    def __init__(self, name, health):
        self.name = name
        self.health = health



    def hit(self, comp_health=100):
        while self.health > 0 and comp_health > 0:
            turn = random.randint(1, 2)
            if turn == 1:
                comp_health -= 20
                print("Вы нанесли урон на 20 очков. Уровень здоровья оппонента: ", comp_health)
            elif turn == 2:
                self.health -= 20
                print("Вам нанесли урон на 20 очков. Уровень Вашего здоровья: ", self.health)

        if self.health == 0:
            print("Вы погибли")

        elif comp_health == 0:
            print("Погиб оппонент")

warrior_1 = Warrior("Бык", 100)
warrior_1.hit()


