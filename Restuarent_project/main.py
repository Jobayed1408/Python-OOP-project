from menu import Pizza, Burger, Drinks, Menu 
from restuarent import Restaurant
from Users import Chef, Customers, Server, Manager
from order import Order

def main():
    menu = Menu()
    
    pizza1 = Pizza('Meat Pizza', 600, 'large', ['meat', 'onion', 'morich'])
    menu.add_menu_item('pizza', pizza1)
    pizza2 = Pizza('Fish Pizza', 400, 'large', ['fish', 'onion'])
    menu.add_menu_item('pizza', pizza2)
    pizza3 = Pizza('Dal Pizza', 300, 'large', ['dal', 'onion'])
    menu.add_menu_item('pizza', pizza3)
    
    # add burger to the menu
    burger1 = Burger('Naga Burger', 1000, 'chicken', ['bread', 'chili']) 
    menu.add_menu_item('burger', burger1)
    burger2 = Burger('Beef Burger', 1200, 'beef', ['bread', 'goru']) 
    menu.add_menu_item('burger', burger2)
    
    # add drinks to the menu 
    coke = Drinks('coke', 50, True)
    menu.add_menu_item('drink', coke)
    coffee = Drinks('Mocha Coffee', 120, False) 
    menu.add_menu_item('drink', coffee) 
    
    # show menu 
    # menu.show_menu()
    
    resturent = Restaurant('Mayer Doa Resturant', 2000, menu)
    
    # add employees
    manager = Manager('Kala Chan Manager', 829348394835, 'kala@chan.com', 'Chadpur', 1500, 'january 1 2020','core')
    
    resturent.add_employee('manager', manager) 
    
    chef = Chef('Guru Doyal', 8293984, 'rustom.com', 'Noakhali', 60, 'February 1 2021', 'fish', 'chef') 
    resturent.add_employee('chef', chef) 
    
    server = Server('Moga server', 948542, 'no.ocm', 'barir kamla', 300, 'jan 15 2023', 'server')
    resturent.add_employee('server' , server)
    
    # show employees 
    # resturent.show_employee()
    
    # Customer 
    Customer1 = Customers('Ali', 8343489, 'ali@.com', 'Jahangirnagar', 15000)
    order1 = Order(Customer1, [pizza3, coffee])
    Customer1.pay_for_order(order1)
    resturent.add_order(order1)
    
    resturent.receive_payment(order1, 2000, Customer1)
    
    print('Revenue and balance after first customer: ', resturent.revenue, resturent.balance) 
    
    Customer2 = Customers('Asfaq', 8343489, 'ali@.com', 'Jahangirnagar', 15000)
    order2 = Order(Customer1, [pizza1, burger1, pizza3, coffee])
    Customer1.pay_for_order(order2)
    resturent.add_order(order2) 
    
    resturent.receive_payment(order2, 3000, Customer2)
    
    print('Revenue and balance after second customer: ', resturent.revenue, resturent.balance) 
    
    # pay rent
    resturent.pay_expense(resturent.rent, 'Rent') 
    print('after rent', resturent.revenue, resturent.balance, resturent.expense)
    
    resturent.pay_salary(server)
    print('after salary', resturent.revenue, resturent.balance, resturent.expense)
           
if __name__ == '__main__':
    main()