from Pet import Pet

class Cat(Pet):
    def __init__(self, name, age):
        super().__init__(name,age)

    def talk(self):
        return "Meeiauuu"

class Dog(Pet):
    def __init__(self, name, age):
        super().__init__(name,age)

    def talk(self):
        return "Wooofff"

def Main():
    star = Dog("Star", 8)
    garfild = Cat("Garfild", 10)
    print(star)
    print(garfild)


if __name__ == "__main__":
    Main()

