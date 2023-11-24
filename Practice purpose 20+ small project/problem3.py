import math 
class Instance:
    def __init__(self, a,b,c):
        self.a = a 
        self.b = b 
        self.c = c 
    def sum(self):
        return self.a + self.b + self.c 
    
    def factorial(self):
        return math.factorial(self.b)
    
result = Instance(2,5,6)
print(result.sum())
print(result.factorial())