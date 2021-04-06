class Books():
    def __init__(self, name, author, year, genre):
        self.name = name
        self.author = author
        self.year = year
        self.genre = genre

    def __repr__(self):
        rep = "Book: " + self.name + ": " + self.author + ": " + self.year + ": " + self.genre
        return  rep

    def __str__(self):
        rep = "Book: " + self.name + ": " + self.author + ": " + self.year + ": " + self.genre
        return rep

    def conparison(self):
        if repr(book1) == str(book1) and repr(book2) == str(book2) and repr(book3) == str(book3):
            print("Равно")
        else:
            print("Не равно")


book1 = Books("Три мушкетера", "А.Дюма", "1844 год", "Роман")
print(str(book1))
book2 = Books("Черный тюльпан", "А.Дюма", "1850 год", "Роман")
print(str(book2))
book3 = Books("Граф Монте-Кристо", "А.Дюма", "1844 год", "Роман")
print(repr(book3))
book1.conparison()
