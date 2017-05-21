class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk (self):
        raise NotImplementedError("Please Implement this method")

    def __str__(self):
        return("Type: "+ str(type(self)) + ", Name: " + self.name + ", age: " + str(self.age) + ", Talk: " + self.talk())

