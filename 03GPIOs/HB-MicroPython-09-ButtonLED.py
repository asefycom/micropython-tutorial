'''
For more details, please follow the link below:
https://hamruyesh.com/product/micro-python-esp32-esp8266-programming-tutorial/

'''
from machine import Pin
from time import sleep

btn = Pin(4, Pin.IN)
led = Pin(5, Pin.OUT)

while True:
    print("btn", btn.value())
    print("led", led.value())
    led.value(btn.value())
    sleep(0.2)