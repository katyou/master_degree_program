# coding:UTF-8
class SendValue:
	"""Sending value of solar and fuel's arduino"""

	def __init__(self):
		self.measure = ""

	#change value if you change serial port(solar_arduino)
	def solarserial(self):
		serialconnect = "/dev/ttyACM0"
		return (serialconnect)

	#change value if you change serial port(fuel_arduino)
	def fuelserial(self):
		serialconnect = "/dev/ttyACM1"
		return (serialconnect)

import time
import serial
import os
import shutil

def serial_iv():
    send = SendValue()  #made instance

    serialconnect = send.solarserial()
    ser = serial.Serial(serialconnect, 9600)
    time.sleep(2)
    ser.write(b"z")
    return(ser)

def serialfinish(ser):
	ser.write(b"y")
	ser.close()

def serialduty(dutyvalue):
    send = SendValue()  #made instance

    serialconnect = send.fuelserial()
    ser = serial.Serial(serialconnect, 115200) #ser is serialwrite.
    time.sleep(2)
    ser.write(bytes([dutyvalue]))
    return(ser)
