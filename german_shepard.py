#from animal import Animal
from dog import Dog
class GermanShepard (Dog):
    def __init__(self) -> None:
        super().__init__()
    def breathe(self):
        super().breathe()
    def walk(self):
        super().walk()
        print("German Shepard's show their beautiful color while running.")
    def summary(self):
        return super().summary()

myGermanShepard=GermanShepard()
myGermanShepard.summary()
print('\n')
myGermanShepard.breathe()
print('\n')
myGermanShepard.walk()
print('=====')

