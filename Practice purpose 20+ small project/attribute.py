class Shop:
    cart = []
    def __init__(self , buyer):
        self.buyer = buyer
    
    def add_to_cart(self, item):
        self.cart.append(item)
        
mahzabeen = Shop('Meh za Been')        
mahzabeen.add_to_cart('shoes')
mahzabeen.add_to_cart('phone')
print(mahzabeen.cart)

nisho = Shop('nisho')
nisho.add_to_cart('hudie')
nisho.add_to_cart('watch')
print(nisho.cart)