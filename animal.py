from abc import ABC,abstractclassmethod
class Animal():
    def __init__(self, numberOfLegs,numberOfEyes) -> None:
        self.NumberOfLegs=numberOfLegs
        self.NumberOfEyes=numberOfEyes
        self.Breath=True
        self.Walk=True
    
    def breathe(self):
        if self.Breath==True:
            print(f'The {self.__class__.__name__} is breathing.')
        else:
            return f"The {__class__.__name__} is Not breathing!"
    
    def walk (self):
        if self.Walk==True:
            print(f'Walking with [{self.NumberOfLegs}] legs.')
        else:
            return "This animal can't walk! "

    def summary (self):
        print(f'This is an instance of [{self.__class__.__name__}]. It has [{self.NumberOfLegs}] legs, and [{self.NumberOfEyes}] eyes.')

myAnimal=Animal(2,2)
#print(myAnimal.summary())
myAnimal.summary()
print('\n')
#print(myAnimal.breathe())
myAnimal.breathe()
print('\n')
#print(myAnimal.walk())
myAnimal.walk()

print('=====')