class Animals:
    pass

class Pets:
    pass

class Dog(Pets):
    @staticmethod 
    def bark():
        print("BowW BowW")

d = Dog()
d.bark()