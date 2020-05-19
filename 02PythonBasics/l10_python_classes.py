'''
For more details, please follow the link below:
https://hamruyesh.com/product/micro-python-esp32-esp8266-programming-tutorial/

'''

class Student:
    
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def details(self):
        print(self.name + " " + str(self.score))
        
        
my_first_student = Student("Asefy", 18.25)
print(my_first_student.name)
my_first_student.details()

my_second_student = Student("Karami", 17)
my_second_student.details()

my_students = [my_first_student, my_second_student]
print(my_students[0].name)
