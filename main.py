class DomesticAnimal:
    def __init__(self, name, type_of_animal):
        self.name = name
        self.type_of_animal = type_of_animal

    def sound(self):
        pass
    def show(self):
        print(f"Ім'я {self.name}")
    def type(self):
        pass
class Dog(DomesticAnimal):
    def sound(self):
        print("Woof!")

    def show(self):
        super().show()

    def type(self):
        print(f"Тип тварини {self.type_of_animal}")

class Cat(DomesticAnimal):
    def sound(self):
        print("Meow!")

    def show(self):
        super().show()

    def type(self):
        print(f"Тип тварини {self.type_of_animal}")

class Parrot(DomesticAnimal):
    def sound(self):
        print("Ку-ка-рі-ку")

    def show(self):
        super().show()

    def type(self):
        print(f"Тип тварини {self.type_of_animal}")

class Hamster(DomesticAnimal):
    def sound(self):
        print("звуки гризуна")

    def show(self):
        super().show()

    def type(self):
        print(f"Тип тварини {self.type_of_animal}")
dog = Dog("Rey", "dog")
dog.sound()
dog.show()
dog.type()