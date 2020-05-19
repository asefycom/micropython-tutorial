'''
For more details, please follow the link below:
https://hamruyesh.com/product/micro-python-esp32-esp8266-programming-tutorial/

'''

from machine import Pin
from time import sleep

motion = False

pir = Pin(14, Pin.IN)
led = Pin(12, Pin.OUT)

def interrupt_handler(pin):
    global motion
    motion = True
    global interrupt_pin
    interrupt_pin = pin

pir.irq(handler=interrupt_handler, trigger=Pin.IRQ_RISING)

while True:
    if motion:
        led.value(1)
        print("Led turned on! Interrupt sent by: ", interrupt_pin)
        sleep(10)
        led.value(0)
        print("Motion Stopped!")
        motion = False