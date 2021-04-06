class Books():
    def __init__(self, name, author, year, genre, reviews):
        self.name = name
        self.author = author
        self.year = year
        self.genre = genre
        self.reviews = reviews

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

    @staticmethod
    def reviews(self):
        if self.name == "Три мушкетера":
            print("Три мушкетера - великолепная книга")
        elif self.name == "Черный тюльпан":
            print("Черный тюльпан - это хоршая книга")
        elif self.name == "Граф Монте-Кристо":
            print("Граф Монте-Кристо книга просто супер")


#Задаю три книги. Вызываю их
book1 = Books("Три мушкетера", "А.Дюма", "1844 год", "Роман", reviews="")
print(str(book1))
book2 = Books("Черный тюльпан", "А.Дюма", "1850 год", "Роман", reviews="")
print(str(book2))
book3 = Books("Граф Монте-Кристо", "А.Дюма", "1844 год", "Роман", reviews="")
print(repr(book3))

#Инициализация проверки на равенство(Честно говоря так толком и не понял, что сравнивать)
book1.conparison()

#Вывожу отзывы на каждую книгу
print("Отзыв о книге №1: ")
Books.reviews(book1)
print("Отзыв о книге №2: ")
Books.reviews(book2)
print("Отзыв о книге №3: ")
Books.reviews(book3)