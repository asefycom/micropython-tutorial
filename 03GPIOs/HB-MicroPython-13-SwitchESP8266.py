from machine import Pin, PWM, ADC
from time import sleep

frequency = 5000

led = PWM(Pin(5), frequency)
pt = ADC(0)

while(True):
    pt_value = pt.read()
    print(pt_value)
    
    if (pt_value < 15):
        led.duty(0)
    else:
        led.duty(pt_value)
        
    sleep(0.1)
        

