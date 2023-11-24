class Bank:
    def __init__(self, holder_name, initial_deposit)->None:
        self.holder_name = holder_name # public class
        self._branch = 'Banani 11' # protected class 
        self.__balance = initial_deposit # private class 

    def deposit(self, amount):
        self.__balance += amount 
        
    def get_balance(self):
        return self.__balance
    
    def withdraw(self , amount):
        print(f'balance = {self.__balance}')
        if amount <= self.__balance:
            self.__balance = self.__balance - amount 
            return amount 
        else :
            return f'No balance'
        
rafsasn = Bank("Choto vai" , 1000)
# print(rafsasn.holder_name) 
# rafsasn.holder_name = 'boro vai'
# print(rafsasn.holder_name )
rafsasn.deposit(400)      
print(rafsasn.get_balance()) 
withdraw = rafsasn.withdraw(500)
print(withdraw)
print(rafsasn._Bank__balance)
        
# print(rafsasn._branch)
        