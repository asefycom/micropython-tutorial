from machine import Pin, ADC
from time import sleep

pt = ADC(Pin(34))
pt.atten(ADC.ATTN_11DB)

while True: 
  print(pt.read())
  sleep(0.3)