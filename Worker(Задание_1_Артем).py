class Worker:

    def __init__(self, name, age, week_day):
        self.name = name
        self.age = age
        self.week_day = week_day

    def work(self):
        if 0 < self.week_day < 6:
            print("На работу иду")
        elif 6 <= self.week_day <= 7:
            print("Юхууу.Выходные!")
        else:
            print("Нет такого дня недели")

worker = Worker("Алексей", "52", 1)
worker.work()