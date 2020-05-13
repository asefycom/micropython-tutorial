#Source.Code.From.HamRuyesh.com

import machine
from machine import Pin
from time import sleep

led = Pin (2, Pin.OUT)
  
led.value(0)
sleep(1)
led.value(1)
sleep(1)

sleep(5)
print('Im awake, but Im going to sleep')
sleep(1)
machine.deepsleep()
