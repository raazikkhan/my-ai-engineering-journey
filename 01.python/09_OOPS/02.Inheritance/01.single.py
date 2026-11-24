class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"Animal name: {self.name}")       
class Dog(Animal):
    def sound(self):
        print(f"{self.name} Barks")        

d = Dog("Tommy")
d.info()
d.sound()        