
class Person:
    id_genarate = 100 
    def __init__(self, email, password):
        self.email = email 
        self.password = password 
        self.user_id = Person.generate_id()
        # Person.id_genarate += 1 
    
    @classmethod
    def generate_id(self): 
        id = self.id_genarate 
        self.id_genarate += 1 
        return id 
        
    def __repr__(self) -> str:
        return f'email {self.email} id: {self.user_id}'
    
    
class Product:
    def __init__(self, name, price, quantity):
        self.name = name 
        self.price = price 
        self.quantity = quantity 
        
    def __repr__(self)->str:
        return f"product name: {self.name} || price: {self.price} || quantity: {self.quantity}"

class Store:
    def __init__(self) -> None:
        self.total_products = {} 
        
    def add_products(self, seller_id, product):
        # print(seller_id)
        # print(vars(product)) 
        productDict = vars(product)
        
        
        if seller_id not in self.total_products: 
            self.total_products[seller_id] = [] 
            
            seller_info = {}
            seller_info['total_sell_products'] = 0 
            seller_info['total_sell_amount'] = 0 
            seller_info['total_profit_amount'] = 0 
            self.total_products[seller_id].append(seller_info)
            
        self.total_products[seller_id].append(productDict) 

    pass 

class Owner(Person):
    def __init__(self, email, password) -> None:
        
        super().__init__(email, password)
        self.total_sell_product = 0 
        self.total_sell_amount = 0 
        self.total_profit_amount = 0 
        
    def shop_info(self, store):
        all_seller_id = store.total_products.keys()
        for id in all_seller_id:
            # print(id)
            sell_info = store.total_products[id][0]
            print(id, sell_info)
            self.total_sell_product += sell_info['total_sell_products']
            self.total_sell_amount += sell_info['total_sell_amount']
            self.total_profit_amount += sell_info['total_profit_amount']
            print(self.total_sell_product)
            print(self.total_sell_amount)
            print(self.total_profit_amount)
            
        sell_info = {
            'total_sell_products': self.total_sell_product,
            'total_sell_amount': self.total_sell_amount,
            'total_profit_amount': self.total_profit_amount
            
            }
        return sell_info
        
        pass

class Seller(Person):
    
    def __init__(self, email, password) -> None:
        super().__init__(email, password)
    
    def add_product(self, product_name, product_price, product_quantity):
        product = Product(product_name, product_price, product_quantity) 
        # print(product) 
        store.add_products(self.user_id, product) 
        
    def sell_info(self, store):
        print(self.user_id)
        print(store.total_products[self.user_id][0])


class Customer(Person):
    def __init__(self, email, password) -> None:
        super().__init__(email, password) 
        self.total_buy_amount = 0 
        self.total_buy_product = 0 
        
    
    def show_products(self, store):
        key = store.total_products.keys()
        for i in key:
            print(i)
            for index in range(1 , len(store.total_products[i])):
                print(store.total_products[i][index])
                pass 
        
        # all_keys = store.total_products.keys()
        # for id in store.total_products.keys():
        #     print('Seller id: ',id)
        #     print('Available Products: ')
        #     for index in range(1, len(store.total_products[id])):
        #         var = store.total_products[id]
        #         print('name: ',var[index]['name'], '\tPrice: ', var[index]['price'], '\tQuantity: ', var[index]['quantity'])
            
            # print('==========s=============') 
                # specific name price or product dekhar jonno 
                # print(product['name'], product['price'])
        # print(all_keys)
        # print(store.total_products)
        
    def buy_product(self, store, seller_id, product_name, quantity):
        # print(store.total_products[seller_id])
        b = True
        for index in range(1, len(store.total_products[seller_id])):
            product = store.total_products[seller_id][index]
            # print(product)
            
            if product['name'] == product_name:
                # print(product)
                if product['quantity'] >= quantity:
                    product['quantity'] -= quantity
                    self.total_buy_product += quantity 
                    prices = quantity*product['price']
                    self.total_buy_amount += prices 
                    print(prices, product['quantity'])
                    b = False
                    
                    seller = store.total_products[seller_id][0]
                    seller['total_sell_products'] += quantity 
                    seller['total_sell_amount'] += prices 
                    seller['total_profit_amount'] += (prices*10 // 100)
                
                else:
                    print(f'Product avalable only: {product['quantity']}')
            
        if b:
            print('The product is not available.')
            
        pass 

store = Store()

seller1 = Seller('s1@gmail.com', 3234)
seller2 = Seller('s2@gmail.com', 2344)
seller3 = Seller('s3@gmail.com', 3242)

seller1.add_product('glass1', 150, 13)
seller1.add_product('glass2', 152, 15)
seller1.add_product('pen', 200, 10)

seller2.add_product('pen1' , 45, 60)
seller2.add_product('pen2' , 65, 45)
seller2.add_product('pen' , 120, 25)

seller3.add_product('pencil' , 65, 42)
seller3.add_product('pencil2' , 55, 12)

customer1 = Customer('c1gmail.com', 123) 
customer2 = Customer('c2gmail.com', 234) 
# # customer1.show_products(store)
customer1.buy_product(store, 100, 'glass1', 5 ) 
# # customer1.show_products(store) 

customer1.buy_product(store, 100, 'glass2', 5 ) 
# # customer1.show_products(store) 

customer2.buy_product(store, 101, 'pen1', 10 ) 
# customer2.show_products(store)
# print(store.total_products)

# seller1.sell_info(store)
# seller2.sell_info(store)
# seller3.sell_info(store)



# print(seller1)
# print(seller2)
# print(seller3)


owner = Owner('owner@gmail.com', 456) 

print('owner ',owner.shop_info(store) )
