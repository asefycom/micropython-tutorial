from machine import Pin, ADC
from time import sleep

pt = ADC(0)

while True: 
  print(pt.read())
  sleep(0.3)