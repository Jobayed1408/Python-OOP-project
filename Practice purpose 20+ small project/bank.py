
class Bank:
    
    def __init__(self , balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000
        
    def get_balance(self):
        return self.balance
    
    def deposit(self , amount):
        if amount > 0:
            self.balance += amount
            print(f'New balance {self.balance}')
            
    def withdraw(self , amount):
        if amount < self.min_withdraw:
            print(f'You can not withdraw below {self.min_withdraw} ')
        elif amount > self.max_withdraw:
            print(f'You can not withdraw above {self.max_withdraw}')
        else:
            self.balance -= amount
            print(f'Here is your money {amount}')
            print(f'New balance {self.get_balance()}')

brac = Bank(150000)
brac.withdraw(25)
brac.withdraw(250000)
brac.withdraw(25000)

dbbl = Bank(5000)
dbbl.deposit(2000)




