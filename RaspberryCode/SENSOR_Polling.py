#!/usr/bin/env python2.7
#########################################################
## Sensor_Polling.py
## Created by Kenny from www.iotbreaks.vn, April 16, 2016.
## Released into the public domain.
## Tutorial: 
#########################################################

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

ledOutPin=17
sensorInPin=18

GPIO.setup(ledOutPin, GPIO.OUT)
GPIO.setup(sensorInPin, GPIO.IN)

num=0
while 1 : 
	readValue = GPIO.input(sensorInPin)
	print(str(num) + "readValue = " + str(readValue))
	num+=1
	GPIO.output(ledOutPin, readValue) 
	time.sleep(0.2)

GPIO.cleanup()