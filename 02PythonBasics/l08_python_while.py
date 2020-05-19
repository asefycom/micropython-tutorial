'''
For more details, please follow the link below:
https://hamruyesh.com/product/micro-python-esp32-esp8266-programming-tutorial/

'''

a = 20
b = 0

while b < a:
    print(b)
    b += 1
    
while True:
    print(b)
    b += 1
    if b == 1000:
        break