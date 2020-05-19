'''
For more details, please follow the link below:
https://hamruyesh.com/product/micro-python-esp32-esp8266-programming-tutorial/

'''
from machine import Pin, ADC
from time import sleep

pr = ADC(Pin(39))
pr.atten(ADC.ATTN_11DB)
led = Pin(12, Pin.OUT)

while(True):
    print(pr.read())
    print("led", led.value())
    
    if (pr.read() < 2000):
        led.value(1)
    else:
        led.value(0)
        
    sleep(0.3)