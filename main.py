# coding:UTF-8

#You must connect arduino of port number "ttyACM0" and "tty ACM1"
#                                         (solar I-V)  (fuelcell)
#if you change port number, you rewrite ard_sending.py

class Measurement:
	"""Measurement solar I-V curve"""

	def __init__(self):
		self.measure = ""

	def changedirgragh(self):
		os.chdir("/home/ienaga/デスクトップ/python_class_sample/graghdata")

	def changedirtxt(self):
		shutil.copy2("/home/ienaga/デスクトップ/python_class_sample//graghdata/sample.txt",
		              "/home/ienaga/デスクトップ/python_class_sample/textdata/sample.txt")
		os.remove('sample.txt')
		os.chdir("/home/ienaga/デスクトップ/python_class_sample/textdata")

	def arduinosolar(self, ser):
		text = open("sample.txt", 'w')
		for i in range (1, 300):
			val = ser.readline()
			print(val.decode('utf-8'))
			text.write(val.decode('utf-8'))
		text.close()

	def plotmeasurement(self):
		from matplotlib import pyplot as plt
		import numpy as np
		import os

		fig = plt.figure()
		xm, ym = np.loadtxt('sample.txt', delimiter = ',', unpack = True)

		#Arduino data => プロットした値を正式な値に変換
		for line in range (1, 300):
			voltage = (xm * 55)/1023
			current = (ym * 5)/(1023 * 11)

		sampledata = [voltage, current]

		fig = plt.figure()
		#decided x and y plot's range.
		plt.xlim([5.5, 23])
		plt.ylim([0, 0.4])
		plt.plot(voltage, current, '-o')

		plt.savefig('sample.png')

		for power in sampledata:
			power = voltage * current

		solar_plt_data = np.array([voltage, current, power])
		#print (solar_plt_data)
		time.sleep(3)

		# #TODO: テスト確認用
		# mpp = 0
		# for i in range (1, 299):
		# 	if mpp <= solar_plt_data[2, i]:
		# 		mpp = solar_plt_data[2, i]
		# 		maxvoltage = solar_plt_data[0, i]
		#
		# print (mpp)
		# print (maxvoltage)
		# time.sleep(1)

		return (solar_plt_data)


	def outputvalue(self, ser):
		os.chdir("/home/ienaga/デスクトップ/python_class_sample/master_degree_program/textdata")

		#HACK: this code may not be good because test code.
		output = open("output.txt", 'w')
		# t.start(variable, voltagein)  #Timer method starts
		for value in range (1, 300):
			valiable = ser.readline()
			print(valiable.decode('utf-8'))
			output.write(valiable.decode('utf-8'))
		output.close()
		# t.cancel()  #Timer method stop

#HACK: this code may not be good because test code.
#Timer method
# def adjustment(valiable, voltagein, mpp): #duty ratio adjustment
# 	arraydata = valiable[pvvoltage, pvcurrent,
# 	                     fcvoltage, fccurrent, power]
# 	if arraydata[:4] <= 1.45:
# 		average = (arraydata[:4] + 1.45) / 2
#
# 		if voltagein <= mpp[:0]:
# 			while (arraydata[:4] < average):
# 				voltagein += 10
# 				duty = 250/(2.5 + voltagein)
# 				ser = serialduty(senddutyvalue)
# 		if voltagein > mpp[:0]:
# 			while (arraydata[:4] < average):
# 				voltagein -= 10
# 				duty = 250/(2.5 + voltagein)
# 				ser = serialduty(senddutyvalue)
#
# 	t = threading.Timer(10.0, adjusutment)
# 	t.start(voltagein)

#This code is Main program!
while True:
	import datetime
	import os
	import shutil
	import time
	import threading

	measure = Measurement() #made instance

	measure.changedirgragh()
	from ard_sending import serial_iv
	ser = serial_iv()

	#arduinosolar function on Measure class
	measure.arduinosolar(ser)  # this method writes I-V datas in sample.txt.

	from ard_sending import serialfinish
	serialfinish(ser)

	#HACK: content class in calculate class(maybe-later)
	sampledata = measure.plotmeasurement()

	#import method of content in calculate class.
	from calculate import content
	senddutyvalue = content(sampledata[0], sampledata[1], sampledata[2], 2.215)
	               #content(  [volatage],    [current],      [power],   idealpower)
	# I decided idealpower by thinking efficiency of electric power.

	from ard_sending import serialduty
	serduty = serialduty(senddutyvalue)

	# #HACK: this code may not be good because test code.
	# t = threading.Timer(target = adjustment)

	measure.outputvalue(serduty)

	measure.changedirgragh()
	dailytime = datetime.datetime.now()
	newname = "{0:%Y-%m-%d-%H-%M:%S}.png".format(dailytime)
	os.rename("sample.png", newname)
	measure.changedirtxt()
	newname = "Fuel:{0:%Y-%m-%d-%H-%M:%S}.txt".format(dailytime)
	os.rename("output.txt", newname)

	time.sleep(20)
