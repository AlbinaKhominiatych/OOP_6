from dataclasses import dataclass


@dataclass
class DomesticAnimal:
    _name: str
    _type_of_animal: str

    def sound(self):
        pass

    def show(self):
        print(f'{self._name}')

    def type_of_animal(self):
        print(self._type_of_animal)


@dataclass
class Dog(DomesticAnimal):
    def sound(self):
        print('Gav-Gav-Gav')


@dataclass
class Cat(DomesticAnimal):
    def sound(self):
        print('Miau-Miau')


@dataclass
class Perrot(DomesticAnimal):
    def sound(self):
        print('Kria-Kria')


@dataclass
class Hamster(DomesticAnimal):
    def sound(self):
        print('Nyam-Nyam')


dog = Dog('Hatiko', 'Dog')
cat = Cat('Matroskin', 'Cat')
parrot = Cat('Kesha', 'Parrot')
hamster = Hamster('Homyak', 'Hamster')

dog.sound()
dog.show()
dog.type_of_animal()