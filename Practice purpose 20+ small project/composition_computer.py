class CPU:
    def __init__(self, cores) -> None:
        self.cores = cores 
        print(self.cores)
class RAM:
    def __init__(self, size) -> None:
        self.size = size 
        print( self.size )
        
class HardDrive:
    def __init__(self, capacity) -> None:
        self.capacity = capacity 
        print(self.capacity)
        
class Computer:
    def __init__(self, cores, ram, hd_size) -> None:
        self.cores = CPU(cores)
        self.ram = RAM(ram) 
        self.hd_size = HardDrive(hd_size) 
        
    
hp = Computer(4, 8 , 256)
# print(hp.cores) 
# print(f'core =  {hp.cores}')
    