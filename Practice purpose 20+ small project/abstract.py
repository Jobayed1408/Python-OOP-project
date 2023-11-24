from abc import ABC, abstractmethod
#  abstract base class

class Animal:
    @abstractmethod
    def eat(self):
        print('i eat food!')
        
    @abstractmethod
    def move(self):
        pass 
    
class Monkey(Animal):
    def __init__(self , name) -> None:
        self.category = 'Monkey'
        self.name = name 
        super().__init__()
    
    def eat(self):
        print('I am eating...')
        
    def move(self):
        print('Moving.')

dragon = Monkey('meat')
dragon.eat()
dragon.move()
    
