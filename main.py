# coding:UTF-8
class Measurement:
	"""Measurement solar I-V curve"""

	def __init__(self):
		self.measure = ""

	def changeserial(self):  #change value if you change serial port.
		serialconnect = "/dev/ttyACM0"
		return (serialconnect)

	def changedirgragh(self):
		os.chdir("/home/ienaga/デスクトップ/python_class_sample/master_degree_program/graghdata")

	def changedirtxt(self):
		shutil.copy2("/home/ienaga/デスクトップ/python_class_sample/master_degree_program/graghdata/sample.txt",
		              "/home/ienaga/デスクトップ/python_class_sample/master_degree_program/textdata/sample.txt")
		os.remove('sample.txt')
		os.chdir("/home/ienaga/デスクトップ/python_class_sample/master_degree_program/textdata")

	def arduinosolar(self):
		serial = open("sample.txt", 'w')
		for i in range (1,300):
			val = ser.readline()
			serial.write(val.decode('utf-8'))
		serial.close()

	def plotmeasurement(self):
		from matplotlib import pyplot as plt
		import numpy as np
		import os

		fig = plt.figure()
		xm, ym = np.loadtxt('sample.txt', delimiter = ',', unpack = True)

		#プロットした値を正式な値に変換
		for line in range (1,300):
			vol = (xm*55)/1023
			cur = (ym*5)/(1023*11)

		sampledata = (vol, cur)

		fig = plt.figure()
		plt.xlim([5.5,23])
		plt.ylim([0,0.4])
		plt.plot(vol, cur, '-o')

		plt.savefig('sample.png')

		for power in sampledata:
			power = vol * cur

		sampledata = np.array([vol, cur, power])
		from calculate import content
		content(vol, cur, power)


import datetime
import serial
import os
import shutil
import time

measure = Measurement()
measure.changedirgragh()

serialconnect = measure.changeserial()
ser = serial.Serial(serialconnect,9600)
time.sleep(2)
ser.write(b'z')

measure.arduinosolar()   #arduinosolar function on Measure class

ser.write(b"y")
ser.close()

measure.plotmeasurement()

dailytime = datetime.datetime.now()
newname = "{0:%Y-%m-%d-%H-%M:%S}.png".format(dailytime)
os.rename("sample.png",newname)

measure.changedirtxt()
