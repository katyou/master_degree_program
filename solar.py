# coding:UTF-8
class Measurement:
	"""Measurement solar I-V curve"""

	def __init__(self):
		self.measure = ""

	def arduinosolar(self):
		serial = open("sample.txt", 'w')
		for i in range (1,300):
			val = ser.readline()
			serial.write(val.decode('utf-8'))


import datetime
import serial
import os
import shutil
import time

ser = serial.Serial("/dev/ttyACM0",9600)
time.sleep(2)
ser.write(b'z')
serial = open("sample.txt", 'w')

ard = Measurement()
ard.arduinosolar()

ser.write(b"y")
serial.close()

from matplotlib import pyplot as plt
import numpy as np
import os

fig = plt.figure()
xm, ym = np.loadtxt('sample.txt', delimiter = ',', unpack = True)

for line in range (1,300):
	vol = (xm*55)/1023
	cur = (ym*5)/(1023*11)

sampledata = (vol, cur)

fig = plt.figure()
plt.xlim([5.5,23])
plt.ylim([0,0.4])
plt.plot(vol, cur, '-o')

plt.savefig('sample.png')

dailytime = datetime.datetime.now()
newname = "{0:%Y-%m-%d-%H-%M:%S}.png".format(dailytime)
os.rename("sample.png",newname)

os.chdir("/home/ienaga/デスクトップ/python_class_sample/sample") #change directly

for power in sampledata:
	power = vol * cur

sampledata = np.array([vol, cur, power])

from calculate import content
content(vol, cur, power)

time.sleep(30.0)

ser.close()
