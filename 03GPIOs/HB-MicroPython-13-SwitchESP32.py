'''
For more details, please follow the link below:
https://hamruyesh.com/product/micro-python-esp32-esp8266-programming-tutorial/

'''
from machine import Pin, PWM, ADC
from time import sleep

frequency = 5000

led = PWM(Pin(5), frequency)
pt = ADC(Pin(34))
pt.width(ADC.WIDTH_10BIT)
pt.atten(ADC.ATTN_11DB)

while(True):
    pt_value = pt.read()
    print(pt_value)
    
    if (pt_value < 15):
        led.duty(0)
    else:
        led.duty(pt_value)
        
    sleep(0.1)
        

