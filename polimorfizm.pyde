class Pet():
    pass
class Dog():
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name + ':woof'
    def __add__(self, other):
        return self.name[0]+other.name[0]
    def __sub__(self, other):
        return self.name+other.name
    
class Cat():
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name + ':meow'
    def __add__(self, other):
        return self.name[0]+other.name[0]
    def __sub__(self, other):
        return self.name+other.name
    

lara = Cat('Lara')
skrypcik = Cat('Skrypcik')
figo = Dog('Figo')
zgaga = Dog('Zgaga')

lista_zwierzat = [lara, skrypcik, figo, zgaga]

for pet in lista_zwierzat:
    print(pet.speak())
print(isinstance(figo, Cat))
print(isinstance(zgaga, Dog))
print(figo + zgaga)
print(lara - skrypcik)
print(isinstance(lara, Cat))
