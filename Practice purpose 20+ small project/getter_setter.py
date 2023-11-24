class User:
    def __init__(self, name, age, money) -> None:
        self._name =  name 
        self._age =  age 
        self.__money = money 
    
    @property
    def age(self):
        return self._age 
# method def salary(self): 
    @property
    def salary(self):
        return self.__money
    
    # def salary(self, value):
    #     pass
    
    # set a value  in a private method by attribute
    @salary.setter
    def salary(self, value):
        if value < 0:
            return 'salary not negetive'
        self.__money += value 

samsu = User('kopa',  21, 12000)
print(samsu.age)
print(samsu.salary) 
# samsu.salary(210)
samsu.salary = 120
print(samsu.salary)

