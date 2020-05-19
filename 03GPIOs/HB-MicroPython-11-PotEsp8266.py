'''
For more details, please follow the link below:
https://hamruyesh.com/product/micro-python-esp32-esp8266-programming-tutorial/

'''
from machine import Pin, ADC
from time import sleep

pt = ADC(0)

while True: 
  print(pt.read())
  sleep(0.3)