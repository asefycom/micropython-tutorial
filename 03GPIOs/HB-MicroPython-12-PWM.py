from machine import Pin, PWM
from time import sleep

led = PWM(Pin(5), freq=5000)

while(True):
    for duty_cycle in range(0, 1024):
        led.duty(duty_cycle)
        sleep(0.005)
        
