#Source.Code.From.HamRuyesh.com

import machine
from machine import Pin
from time import sleep

led = Pin(12, Pin.OUT)

led.value(1)
sleep(1)
led.value(0)
sleep(1)

sleep(5)

print("I am awake, but I am going to sleep deeply!")


machine.deepsleep(10000)
