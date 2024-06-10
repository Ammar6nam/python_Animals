from animal import Animal
class Dog(Animal):
    def __init__(self) -> None:
        super().__init__(numberOfLegs=4, numberOfEyes=2)
    def breathe(self):
        super().breathe()
        print('Dogs love to breathe with their mouths open.')
    def walk(self):
        super().walk()
        print('Dogs love to run.')
    def summary (self):
        super().summary()


myDog=Dog()
myAnimal=Animal(numberOfLegs=2, numberOfEyes=2)
# print(myAnimal)

#print(myAnimal.summary(),myAnimal.breathe(),myAnimal.walk(),sep='/n')
#name=myDog.AnimalName
# print(name)
myDog.summary()
print('\n')
myDog.breathe()
print('\n')
walk=myDog.walk()
print('=====')

