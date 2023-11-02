class Person:
    id_genarate = 100 
    def __init__(self, name, email, password):
        self.name = name 
        self.email = email 
        self.password = password 
        
    def __repr__(self) -> str:
        return f'email {self.email} id: {self.user_id}'

class Account(Person):
    def __init__(self, name, email, password, balance):
        super().__init__(name, email, password) 
        self.balance = balance 
        
    def __repr__(self) -> str:
        return f'name {self.name} email {self.email} password {self.password} '
        

class User(Person):
    def __init__(self, username, password, phone_number):
        self.username = username
        self.password = password 
        self.phone_number = phone_number
        self.total_balance = 0 
        self.total_loan = 0 
        self.user_wallet = 0 
        self.user_account = [] 
        self.transaction_details = {}
        self.new_account = {}
        self.loan_control = True 
    
    def create_account(self, name,  email, password, user_wallet = 0): 
        
        self.user_wallet = 0  
        
        
        account = Account(name, email , password, user_wallet)
        ac = vars(account)
        
        if email not in self.new_account: 
            self.new_account[email] = [] 
            self.new_account[email].append(ac)
            # print(self.new_account) 
            # print(f'Hi {name} your account has been successfully created.')
            # print('Here is your account details')
            # print('==============================')
            # print(self.new_account[email])
        else:
            print('The email is already exist! please try different email!')
        pass 

    def deposit(self,email, amount):
        self.total_balance += amount 
        self.user_wallet += amount 
        key = self.new_account.keys()
        for i in key:
            for index in range(0 , len(self.new_account[i])): 
                if email in self.new_account[i][index]['email']:
                    self.new_account[i][index]['balance'] += amount
                    print(f'Thank you {self.new_account[i][index]['name']} Successfully deposit {self.new_account[i][index]['balance']} ')
                    add = { 'transaction' : f'Deposit {amount} New balance: {self.new_account[i][index]['balance']}' }
                    if i not in self.transaction_details:
                        self.transaction_details[i] = []
                    self.transaction_details[i].append(add)

    def withdraw(self, email, password, amount):
        key = self.new_account.keys()
        find = True
        for i in key:
            # print(i)
            for index in range(0 , len(self.new_account[i])): 
                # print(self.new_account[i][index]['email'])
                if email in self.new_account[i][index]['email']:
                    if password == self.new_account[i][index]['password']:
                        
                        # print(amount)
                        # print(f'CUrrent total {self.total_balance}')
                        # print(f'current {self.new_account[i][index]['balance']}' )
                        self.new_account[i][index]['balance'] -= amount
                        # print(f'Now {self.new_account[i][index]['balance']}' )
                        self.total_balance -= amount 
                        print(f'Successfully withdraw {amount} new balance is: {self.new_account[i][index]['balance']}')
                        add = { 'transaction' : f'Withdraw {amount} New balance: {self.new_account[i][index]['balance']}' }
                        if i not in self.transaction_details:
                            self.transaction_details[i] = []
                        self.transaction_details[i].append(add)
                        find = False
                pass 
                
        if find:
            print('The bank is bankrupt.')
        print(self.new_account)
    
    def check_balance(self,email):
        key = self.new_account.keys()
        find = True
        for i in key:
            for index in range(0 , len(self.new_account[i])): 
                if email in self.new_account[i][index]['email']:
                    info = self.new_account[i][index] 
                    print(f'Hi {info['name']} your account balance is {info['balance']}')
                    # print(  )
                    find = False
                pass 
        if find:
            print("Account doesn't exist.")
    
    def transfer_funds(self, sender, amount, recipient_email):
        key = self.new_account.keys()
        find = True
        for i in key:
            # print(i)
            for index in range(0 , len(self.new_account[i])): 
                # print(self.new_account[i][index]['email'])
                if recipient_email in self.new_account[i][index]['email']:
                    # print(i)
                    # self.new_account[i][index]['balance'] + amount)
                    # print('Yes')
                    # print(amount)
                    print(f'Transfer founds {amount} from {self.new_account[i][index]['name']} to {self.new_account[sender][index]['name']}. New balance of {self.new_account[i][index]['name']}: {self.new_account[i][index]['balance']}')
                    self.new_account[i][index]['balance'] += amount
                    self.new_account[sender][index]['balance'] -= amount
                    add = { 'transaction' : f'Transfer founds {amount} to {self.new_account[i][index]['name']} ' }
                    receive = { 'transaction' : f'Receive TK {amount} from {self.new_account[sender][index]['name']} ' }
                    if i not in self.transaction_details:
                        self.transaction_details[sender] = []
                    self.transaction_details[sender].append(add)
                    self.transaction_details[i].append(receive)
                    
                    # print(add)
                    find = False
                pass 
        if find:
            print("Account doesn't exist.")
       
        # print(f'funds {self.new_account}')
    
    def transaction_history(self, email):
        print(self.transaction_details[email])
        
        # check_balance()
        pass 
    
    
    def login(self, email, password):
        key = self.new_account.keys()
        find = True
        for i in key:
            # print(i)
            for index in range(0 , len(self.new_account[i])): 
                # print(self.new_account[i][index]['email'])
                if email in self.new_account[i][index]['email']:
                    if password == self.new_account[i][index]['password']:
                        print(f'Hi {self.new_account[i][index]['name']}! Thank you for login.')
                        find = False
                pass 
                
        if find:
            print('Invalid email or password!')


    def view_account_details(self, email, password):
        self.login(email, password)
        print(f'Hi {self.username}! Your name is {self.username}, your phone number is {self.phone_number} your account balance is {self.user_wallet} ')
        # Display the user's account details
        # self.create_account()
        # key = self.new_account.keys()
        # for i in key:
        #     print(i)
        #     for index in range(1 , len(self.new_account[i])):
        #         print(self.new_account[i][index])
        #         pass 
        # pass
        

    def change_password(self, email, current_password, new_password):
        # Logic to change the user's password
        key = self.new_account.keys()
        find = True
        for i in key:
            # print(i)
            for index in range(0 , len(self.new_account[i])): 
                # print(self.new_account[i][index]['email'])
                if email in self.new_account[i][index]['email']:
                    if current_password == self.new_account[i][index]['password']:
                        self.new_account[i][index]['password'] = new_password
                        print(f'Hi {self.new_account[i][index]['name']}. Successfully changed password!')
                        find = False
                pass 
                
        if find:
            print('Invalid email or password!')
        pass
    
    def take_loan(self, email, amount, due_date):
        if not self.loan_control:
            print('Sorry! loan service is not available right now')
            return ''
        else: 
            self.due_date  = due_date 
            key = self.new_account.keys()
            find = True
            for i in key:
                # print(i)
                for index in range(0 , len(self.new_account[i])): 
                    info = self.new_account[i][index]
                    if email in self.new_account[i][index]['email']:
                        if amount < info['balance'] * 2 and amount < self.total_balance:
                            
                            self.total_loan += amount   
                            self.total_balance -= amount 
                            print(f'Successfully loaned TK {amount}')
                            print(f'Please give your loan before {due_date}')
                            add = { 'transaction' : f'Take loan {amount} by {self.new_account[i][index]['name']}' }
                            if i not in self.transaction_details:
                                self.transaction_details[i] = []
                            self.transaction_details[i].append(add)
                    
                            find = False
                    pass 
                    
            if find:
                print('You cann\'t loan of TK ',amount)
            # print(self.transaction_details)

class Admin(User):
    def __init__(self, username, password, phone_number, email):
        super().__init__(username, password, phone_number) 
        self.email = email 
        self.admin_account = {}
        
    
    def create_admin_account(self, user):
        admin = Account(self.username, self.email, self.password, user.total_balance) 
        ac = vars(admin)
        
        if self.email not in self.admin_account: 
            print('yes')
            self.admin_account[self.email] = [] 
            self.admin_account[self.email].append(ac)
        else:
            print('Account already exist.') 
        print(self.admin_account) 
    
    def check_available_balance(self):
        print(f'{user.total_balance}') 
        
        pass 
    
    def check_total_loan(self):
        print(f'Total available loan is: {user.total_loan}')
    
    def loan_on_of(self, booli):
        if not booli:
            user.loan_control = False 
    
    


user = User('user', 123, 183897)
user.create_account('Jobayed','jobayed@gmail.com', 123) 
user.create_account('Ahmed','ahmed@gmail.com', 345) 
user.create_account('Sanjid','sanjid@gmail.com', 234) 

user.deposit('jobayed@gmail.com',2000)
user.deposit('sanjid@gmail.com',8344)
user.deposit('ahmed@gmail.com', 2500)
user.deposit('jobayed@gmail.com',2000)
user.deposit('ahmed@gmail.com', 2500)

user.withdraw('ahmed@gmail.com', 345, 1100)
user.check_balance('jobayed@gmail.com')
user.check_balance('sanjid@gmail.com')
user.check_balance('ahmed@gmail.com')
user.transfer_funds('jobayed@gmail.com', 1250, 'ahmed@gmail.com')
user.transaction_history('jobayed@gmail.com')
user.transaction_history('ahmed@gmail.com')

user.login('ahmed@gmail.com', 345)
user.login('jobayed@gmail.com', 123)
user.login('sanjid@gmail.com', 234)
user.change_password('ahmed@gmail.com', 345, 111)
user.login('ahmed@gmail.com', 111)
user.take_loan('jobayed@gmail.com', 530, 'dec 31 2023')
admin = Admin('mehrab',222, 183897, 'nahir@gmail.com')
admin.create_admin_account(user) 
admin.check_total_loan() 
admin.loan_on_of(False)
user.take_loan('ahmed@gmail.com', 1000, 'Dec 25 2023')
user.take_loan('jobayed@gmail.com', 530, 'dec 31 2023')


user.transaction_history('jobayed@gmail.com')
user.transaction_history('sanjid@gmail.com')
user.transaction_history('ahmed@gmail.com')

user.check_balance('jobayed@gmail.com')
user.check_balance('ahmed@gmail.com')
user.check_balance('ahmed@gmaildf.com')
