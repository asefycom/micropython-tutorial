'''
For more details, please follow the link below:
https://hamruyesh.com/product/micro-python-esp32-esp8266-programming-tutorial/

'''

students_1 = {"asefy":18 , "rezaei":15, "karami":20}
students_2 = {"hosseini":20, "homayun":20, "amiri":17}


        
        
def get_best_students(students):
    
    best_list = []
    for key,value in students.items():
        if value == 20:
            best_list.append(key)
    
    return best_list        
            
print(get_best_students(students_1))

if len(get_best_students(students_1)) != 0:
    print(get_best_students(students_1)[0])
else:
    print("Not a Good Class!")


