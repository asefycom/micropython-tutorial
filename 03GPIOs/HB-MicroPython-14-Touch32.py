'''
For more details, please follow the link below:
https://hamruyesh.com/product/micro-python-esp32-esp8266-programming-tutorial/

'''
from machine import Pin, TouchPad
from time import sleep

touch = TouchPad(Pin(4))

while(True):
    print(touch.read())
    sleep(0.1)