def call():
    print('calling someone')
    return 'call done'

class Phone:
    price = 120000
    color = 'blue'
    brand = ' samsung'
    features = ['camera' , 'speaker' , 'hammer'] 
    
    def call(self):
        print('calling one person')

    def send_sms(self , number , sms):
        text = f'sending SMS to : {number} and message: {sms}'
        return text
    
my_phone = Phone()
print(my_phone.features)
# my_phone.call()
result = my_phone.send_sms(40943 , 'hello bro! ') 
print(result)