'''
For more details, please follow the link below:
https://hamruyesh.com/product/micro-python-esp32-esp8266-programming-tutorial/

'''

import math

class Rectangle:
    
    def __init__(self, height, width):
        self.height = height
        self.width = width
        
    def area(self):
        return self.height * self.width
    
    
class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return self.radius * self.radius * math.pi
        
    