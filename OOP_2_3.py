class One:

    def first(self):
        print("First class method")

class Two:

    def second(self):
        print("Second class method")

class Three(One, Two):

    def third(self):
        print("Third class method")

obj = Three()
obj.first()
obj.second()
obj.third()


