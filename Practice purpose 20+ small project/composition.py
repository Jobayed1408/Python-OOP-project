class Engine:
    def __init__(self) -> None:
        pass 
    
    def start(self):
        print( "Engine started" )

class Driver:
    def __init__(self) -> None:
        pass 

class Car:
    def __init__(self)->None:
        self.engine = Engine()
        self.drive  = Driver() 
    
    def start(self):
        self.engine.start()
        
bus = Car()
bus.start()