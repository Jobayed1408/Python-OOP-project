class Person:
    def __init__(self, name, age, height, weight) ->None:
        self.name = name 
        self.age = age 
        self.height = height 
        self.weight = weight 
    def eat(self):
        print('Khawa foroz')
        
    def exercise(self):
        raise NotImplementedError # override
        print('majhemoddhe kora dorkar')

class Cricketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team
        super().__init__(name, age, height, weight) 
    def eat(self):
        print('Niomito pustikor khabar khete hobe')
    def exercise(self): # override
        print('Tuamke kora lagbei')
    
sakib = Cricketer('sakib', 32, 5.11, 74, 'BD')
sakib.eat()
sakib.exercise()

