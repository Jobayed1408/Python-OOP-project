# # base class , parent class

# class BaseClass:
#     pass

# # derived class or child class
# class DerivedClass(BaseClass):
#     pass

class Vehicle:
    def __init__(self, name , price) -> None:
        self.name = name 
        self.price = price 
        
    def move(self):
        print('Moving')
    
class Bus(Vehicle):
    def __init__(self, name, price, seat) -> None:
        self.seat = seat 
        super().__init__(name , price)
    
    def __repr__(self) -> str:
        return super().__repr__()
        
class Truck(Vehicle):
    def __init__(self, name, price, weight) -> None:
        self.weight = weight 
        super().__init__(name, price) 
        
class PickUpTruck(Truck):
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price, weight)

class AcBus(Bus):
    def __init__(self, name, price, seat, temperature) -> None:
        self.temperature = temperature
        super().__init__(name, price, seat) 
        
a = AcBus('ac',1000000,24,25)
a.move()