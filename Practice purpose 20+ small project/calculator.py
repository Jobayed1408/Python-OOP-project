
class Calculator:
    brand = "Casio RS991fx"
    
    def add(self , n , m):
        result = n + m
        return result
    
    def sub(self , n ,m):
        result = n - m
        return result 
    
    def mul(self , n , m):
        result = n * m
        return result
    
    def div(self , n , m):
        result = n // m
        return result
    
my_calculator = Calculator()
add = my_calculator.add(4,2)
print(add)
sub = my_calculator.sub(4,2)
print(sub)
mul = my_calculator.mul(4,2)
print(mul)
div = my_calculator.div(4,2)
print(div)