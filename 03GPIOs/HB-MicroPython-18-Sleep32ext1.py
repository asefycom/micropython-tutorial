#Source.Code.From.HamRuyesh.com

import machine
import esp32
from machine import Pin
from time import sleep

btn1 = Pin(14, mode=Pin.IN)
btn2 = Pin(12, mode=Pin.IN)


esp32.wake_on_ext1(pins=(btn1, btn2), level=esp32.WAKEUP_ANY_HIGH)

print("Going to sleep in 10 seconds!")

sleep(10)

machine.deepsleep()


