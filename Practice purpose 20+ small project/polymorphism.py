# poly --> many(multiple)
# morph --> shape

class Animal:
    def __init__(self, name) -> None:
        self.name=  name
        
    def make_sound(self):
        print('sound')
    
class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print('meow meow ')

class Dog(Animal):
    def __init__(self, name) ->None:
        super().__init__(name)
        
    def make_sound(self):
        print('gheu gheu')
    
class Goat(Animal):
    def __init__(self , name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print('beh beh beh')

don = Cat('don')
don.make_sound()
dog = Dog('non')
dog.make_sound()
got = Goat('chagol')
got.make_sound()
animals = [don, dog, got]
for i in animals:
    i.make_sound()