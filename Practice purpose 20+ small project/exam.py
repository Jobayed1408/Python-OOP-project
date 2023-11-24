class Exam:
    
    def __init__(self  , room):
        # self.total_student = total_student
        self.room = room 
        self.capacity = 50
        self.total = 0
    
    def present_student(self , amount):
        if amount > self.capacity:
            print(f'Maximum student capacity is {self.capacity}')
        if amount <= self.capacity:
            self.total += amount
            print(f'total student {self.total}')

    def total_fees(self , amount):
        print(self.total)
        total = self.total * amount
        print(f'total collected fee {total}')
    
bgc = Exam(1)
bgc.present_student(45)
bgc.present_student(450)
bgc.total_fees(10)
