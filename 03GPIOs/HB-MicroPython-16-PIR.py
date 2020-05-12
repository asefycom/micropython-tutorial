#Source.Code.From.HamRuyesh.com

from machine import Pin
from time import sleep

motion = False

def handle_interrupt(pin):
  global motion
  motion = True
  global interrupt_pin
  interrupt_pin = pin 

led = Pin(12, Pin.OUT)
pir = Pin(14, Pin.IN)

pir.irq(handler=handle_interrupt, trigger=Pin.IRQ_RISING)

while True:
  if motion:
    print('LED turned on! Interrupt Pin is: ', interrupt_pin)
    led.value(1)
    sleep(10)
    led.value(0)
    print('Motion stopped!')
    motion = False