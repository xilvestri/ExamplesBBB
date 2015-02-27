#!/usr/bin/python
import Adafruit_BBIO.GPIO as GPIO
import time

LED = "P8_17"
GPIO.setup(LED,GPIO.OUT)

while(1):
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(LED,GPIO.LOW)
    time.sleep(1)
   
    
if KeyboardInterupt:
     GPIO.cleanup
