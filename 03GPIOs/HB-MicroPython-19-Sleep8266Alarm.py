'''
For more details, please follow the link below:
https://hamruyesh.com/product/micro-python-esp32-esp8266-programming-tutorial/

'''

import machine
from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

def deep_sleep(msecs):
  rtc = machine.RTC()
  rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
  rtc.alarm(rtc.ALARM0, msecs)
  machine.deepsleep()
  
led.value(1)
sleep(1)
led.value(0)
sleep(1)

sleep(5)
print('Im awake, but Im going to sleep')
deep_sleep(10000)