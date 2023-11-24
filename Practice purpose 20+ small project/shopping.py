class Shopping:
    def __init__(self , name):
        self.name = name
        self.cart = []
        
    def add_to_cart(self , item , price , quantity):
        product = {'item': item , 'price': price , 'quantity': quantity}
        self.cart.append(product ) 

    def remove_item(self , item):
        print(item)
        # for name in self.cart:
        #     if name == item:
        # self.cart.remove(item)
            # else:
            #     print('No equal')

    def checkout(self , amount):
        total = 0
        for item in self.cart:
            # print(item)
            total += item['price'] * item['quantity']
            # list1.append(item[item]) 
        print('Total price ' , total)
        
        if amount < total:
            print(f'plz provide {total - amount} more')
        else:
            print(f'Here is ur item and extra money {amount - total}')
shopon = Shopping("Alan shopon")
shopon.add_to_cart('rice ', 120 , 2)
shopon.add_to_cart('Egg' , 12 , 24)
shopon.add_to_cart('Pen' , 12 , 5)
shopon.remove_item('Egg')
print(shopon.cart)
shopon.checkout(600)
