'''
For more details, please follow the link below:
https://hamruyesh.com/product/micro-python-esp32-esp8266-programming-tutorial/

'''

from machine import Pin
from time import sleep

led = Pin(5, Pin.OUT)

while True:
  led.value(not led.value())
  sleep(1)
