class Student:
    
    def __init__(self , name , current_class , id):
        self.name = name
        self.id = id
        self.current_class = current_class
    
    def __repr__(self) -> str:
        return f'Student with name: {self.name} , class: {self.current_class} , id: {self.id}'

class Teacher:
    def __init__(self , name , subject , id) -> None:
        self.name = name
        self.subject = subject
        self.id = id
    def __repr__(self) ->str:
        return f'Teacher: {self.name} , subject: {self.subject} id: {self.id}'

class School:
    def __init__(self, name ) -> None:
        self.name = name
        self.teachers = []
        self.students = []
    
    def add_teacher(self , name , subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name , subject, id)
        self.teachers.append(teacher)
    
    def enroll(self ,name , fee):
        if fee < 6500:
            return 'Not enough fee'
        else:
            id = len(self.students) + 1
            student = Student(name , 'C' ,id )
            self.students.append(student)
            return f'{name} is enrolled with id: {id}, extra money {fee - 6500}'

    def __repr__(self) -> str:
        print('Welcome to' , self.name)
        print('--------OUR TEACHERS-------')
        for i in self.teachers:
            print(i)
        print('------ OUR STUDENTS --------')
        for i in self.students:
            print(i)
        return 'All done!'
        
# alia = Student('Alia torkari' , 9, 1)
# ranvir = Teacher('Ranver ahmed' , 'Algorithm' , 101)
# print(alia)
# print(ranvir)

phitron = School('Phitron')
phitron.enroll('alia' , 5200)
phitron.enroll('rani' , 8000)
phitron.enroll('ashik' , 7000)
phitron.enroll('rani' , 80000)

phitron.add_teacher('tom cruise' , 'DS')
phitron.add_teacher('Adam' , 'Algo')
phitron.add_teacher('Fakhar' , 'DB')

print(phitron)