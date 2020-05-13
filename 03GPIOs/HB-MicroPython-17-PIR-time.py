#Source.Code.From.HamRuyesh.com

from machine import Pin
from time import sleep, time

motion = False
start_timer = False
last_motion_time = 0
delay_interval = 10

pir = Pin(14, Pin.IN)
led = Pin(12, Pin.OUT)

def interrupt_handler(pin):
    global motion, interrupt_pin, last_motion_time, start_timer
    motion = True
    interrupt_pin = pin
    last_motion_time = time()
    start_timer = True

pir.irq(handler=interrupt_handler, trigger=Pin.IRQ_RISING)

while True:
    if motion and start_timer:
        led.value(1)
        print("Led turned on! Interrupt sent by: ", interrupt_pin)
        start_timer = False
    elif motion and (time() - last_motion_time) > delay_interval:  
        led.value(0)
        print("Motion Stopped!")
        motion = False