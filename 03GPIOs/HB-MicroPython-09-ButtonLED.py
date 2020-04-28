from machine import Pin
from time import sleep

btn = Pin(4, Pin.IN)
led = Pin(5, Pin.OUT)

while True:
    print("btn", btn.value())
    print("led", led.value())
    led.value(btn.value())
    sleep(0.2)