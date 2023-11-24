# class Phone:
#     manufacture = "China"
     
#     def __init__(self , owner , brand , price):
#          self.owner = owner
#          self.brand = brand
#          self.price = price
         
#     def send_sms(self , phone , sms):
#         text = f'sending sms from: {phone} to {sms}'
#         print(text)
    
# my_phone = Phone('Jobayed' , 'Oppo' , 9800 )
# print(my_phone.owner , my_phone.brand , my_phone.price)
# dad_phone = Phone('Abbu' , 'samsung' , 12800 )
# print(dad_phone.owner , dad_phone.brand , dad_phone.price)

# my_phone.send_sms( 2302 , 'Hello')


class Pen:
    model = 'Meador'
    
    def __init__(self , name , price):
        self.name = name
        self.price = price
        
    def total_cost(self , cost , total , monthlyUse):
        text = f'total cost {cost} , use {total} , monthly {monthlyUse}'
        print(text)
my_pen = Pen("All time" , 8)
print(my_pen.name , my_pen.price) 
