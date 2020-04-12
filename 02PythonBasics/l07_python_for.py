  
for i in range(1, 10):
    print(i)
    
    
for i in range(1,200):
    if i % 5 == 0:
        print("HOB") # continue    break
    else:
        print(i)
        
        
names = ["asefy", "rezaei", "karami"]

for name in names:
    print(name)
    
        
students = {"asefy":18 , "rezaei":15, "karami":20}

for key,value in students.items():
    #print(key + ":" + str(value))
    if value == 20:
        print("The best student in the class is " + key)
    
    
    