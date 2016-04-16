#!/usr/bin/env python2.7
#########################################################
## Sensor_Interrupt.py
## Created by Kenny from www.iotbreaks.vn, April 16, 2016.
## Released into the public domain.
## Tutorial: 
#########################################################

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

ledOutPin=17
sensorInPin=18
readValue=0 # default is 0 as sensor deactivated

GPIO.setup(ledOutPin, GPIO.OUT)
GPIO.setup(sensorInPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  

def doutSensorDidChange(pin):
	print("Detect changed of Gas sensor to " + str(GPIO.input(sensorInPin)))
	readValue = GPIO.input(sensorInPin)
	GPIO.output(ledOutPin, readValue)

GPIO.add_event_detect(sensorInPin, GPIO.BOTH, callback=doutSensorDidChange)
	
try:
	GPIO.output(ledOutPin, readValue)
	print("Detecting....")
	raw_input("Press anykey to finish>")  

except KeyboardInterrupt:  
    GPIO.cleanup() # clean up GPIO on CTRL+C exit 

GPIO.cleanup()