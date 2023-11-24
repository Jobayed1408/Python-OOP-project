class Shopping:
    cart = [] 
    origin = 'china'

    def __init__(self, name) -> None:
        self.name = name 
    
    @staticmethod   
    def multiply(a, b): # static method without self parameter
        print(a * b)
        
    @classmethod
    def purchase(self, item, price, amount): # class method   
        remaining = amount-price 
        print(f'after buying "{item}\' " ramining balance is {remaining}') 
    
selpi = Shopping('So nar gao')
selpi.purchase('botolota', 10, 100)
# Shopping.purchase('sjkad','alu', 10, 40)
Shopping.purchase('alu', 10, 40)
selpi.multiply(3,4)
selpi.multiply(5,7)