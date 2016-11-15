# coding:UTF-8
class CalculateDuty:
	"""Caluculate duty ratio in fuel cell"""

	def __init__(self):
		self.measure = ""

	def changeserial(self):  #change value if you change serial port.
		serialconnect = "/dev/ttyACM1"
		return (serialconnect)

	def dutycalculation1(self, data):
		for x in range (1, 299):
			index = data[x, 2]  #electric power value

			if index == 1.445:     #取り出したい電力の値 part1
				voltagein = data[x, 0]
				duty = 250/(2.5 + voltagein)
				#sendingvalue = duty * 1023
				print ("No.1")
				print (str(duty))
				time.sleep(5)
				return (duty)
				break

			else:
				x += 1
		return (index)

	def dutycalculation2(self, a):
		nextvalue = np.round(a, 1)
		datathree = np.transpose(nextvalue)
		sample = open("test2.txt", "w")
		sample.write(str(datathree))
		sample.close()

		for z in range (1, 299):
			index = datathree[z, 2]

			if index == 1.45:      #取り出したい電力の値 part 3
				voltagein = datathree[z, 0]
				duty = 250/(2.5 + voltagein)
				#sendingvalue = duty * 1023
				print ("No.3")
				print (str(duty))
				time.sleep(5)
				return (duty)
				break
			else:
				z += 1
		return (index)

	def dutycalculation3(self, a):
		nextvalue = np.round(a, 2)
		datafinish = np.transpose(nextvalue)
		k = 1
		sample = 0
		voltagein = 0

		for k in range (1, 299):
			index = datafinish[k, 2]
			if sample < index and index <= 2.35:
				sample = index
				voltagein = datafinish[k, 0]
			else:
				k += 1

		if voltagein is None:
			voltagein = 10
		duty = 250/(2.5 + voltagein)    #duty*100 => arduino/100 because 1byte sending.
		#sendingvalue = duty * 1023

		print ("No.4")
		print (str(duty))
		time.sleep(3)
		return (duty)

	def outputvalue(self, ser):
		os.chdir("/home/ienaga/デスクトップ/python_class_sample/master_degree_program/textdata")
		output = open("output.txt", 'w')
		for value in range (1, 300):
			val2 = ser.readline()
			print(val2.decode('utf-8'))
			output.write(val2.decode('utf-8'))
		output.close()

import numpy as np
from math import floor
from math import ceil
import time
import serial
import os
import shutil

#content function import from superclass.
def content(volta, currenting, powering):


	dutymeasure = CalculateDuty()  #class declare

	a = np.array([volta, currenting, powering])
	support = np.round(a, 3)
	data = np.transpose(support)

	sample = open("test.txt", "w")
	sample.write(str(data))
	sample.close()

	multivalue = dutymeasure.dutycalculation1(data)

	if multivalue != 2.708:
		multivalue = dutymeasure.dutycalculation2(a)

	if multivalue != 2.771 and multivalue != 2.77:
		if multivalue != 2.8:
			multivalue = dutymeasure.dutycalculation3(a)

	senddutyvalue = int(multivalue)
	# dutying = str(duty) + '\r\n'
	print (senddutyvalue)

	serialconnect = dutymeasure.changeserial()
	ser = serial.Serial(serialconnect, 115200)
	time.sleep(2)
	ser.write(bytes([senddutyvalue]))

	dutymeasure.outputvalue(ser)


# gragh 表示,保存するためのメソッド 今回使用しない
def graphmodel():
  from matplotlib import pyplot as plt
  import numpy as np
  import time
  import os
  import datetime

  fig = plt.figure()

  plt.xlim([5.5, 23])
  plt.ylim([0, 0.3])
  plt.plot(voltage, current, '-o')

  s.chdir("/home/ienaga/デスクトップ/python_class_sample/gragh") #change directly

  plt.savefig('sample.png')

  #text file calculate finish

  dailytime = datetime.datetime.now()
  newname = "{0:%Y-%m-%d-%H-%M:%S}.png".format(dailytime)
  os.rename("sample.png",newname)

  os.remove('sample.txt')
