class Product:
    def __init__(self, name , price):
        self.name = name 
        self.price = price 
    
    # def __repr__(self) ->str:
    #     return f'Product name : {self.name} , Price: {self.price}'


class Shop:
    def __init__(self, name):
        self.name = name 
        self.card = [] 
        self.stock = [] 
        
    def add_product(self,id, product_name, quantity , total_present):
        # def add_to_cart(self , item , price , quantity):
        product = {'id': id, 'item': product_name , 'quantity': quantity, 'available' : total_present } 
        self.stock.append(product) 
        # print(self.stock)
        
    def buy_product(self, idd, name, amount):
        booli = 0
        for i in self.stock:
            # print(f'name = {name} , product name = {i['item']}') 
            if idd == i['id']:
                booli = 1
                if amount <= i['available']:
                    product = {'item': name, 'buy': amount}
                    print('Congress!')
                self.card.append(product) 
                i['available'] -= amount 
                print(f'After buying {i['item']} availalbe is {i['available']}')
            # else:
            #  
        if booli == 0:
            print(f'The {name} is not available')   
            # pass 
        
alia = Shop('Dorkari ponno')
alia.add_product(1, 'komola ', 5, 10)
alia.add_product(2, 'lebu ', 3, 10)
alia.buy_product(1, 'komola', 3) 
alia.buy_product(2, 'lebu', 5)
