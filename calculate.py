# coding:UTF-8
class CalculateDuty:
	"""Caluculate duty ratio of fuel cell"""

	def __init__(self):
		self.measure = ""

	def dutycalculation1(self, array, idealpower):
		support = np.round(array, 3)
		data = np.transpose(support)
		sample = open("test.txt", "w")
		sample.write(str(data))
		sample.close()

		for x in range (1, 299):
			index = data[x, 2]  #electric power value

			if index == idealpower:     #取り出したい電力の値 part1
				voltagein = data[x, 0]
				duty = 250/(2.5 + voltagein)
				print ("No.1")
				print (str(duty))
				time.sleep(5)
				return (duty)

		return (index)

	def dutycalculation2(self, array, idealpower):
		nextvalue = np.round(array, 2)
		datathree = np.transpose(nextvalue)

		#test code
		sample = open("test2.txt", "w")
		sample.write(str(datathree))
		sample.close()

		for z in range (1, 299):
			index = datathree[z, 2]

			if index == idealpower:      #取り出したい電力の値 part 3
				voltagein = datathree[z, 0]
				duty = 250/(2.5 + voltagein)
				print ("No.2")
				print (str(duty))
				time.sleep(5)
				return (duty)
		return (index)

	def dutycalculation3(self, array, idealpower, idealpower3):
		nextvalue = np.round(array, 1)
		datafinish = np.transpose(nextvalue)
		k = 1
		sample = 0
		voltagein = 0

		for k in range (1, 299):
			index = datafinish[k, 2]
			if sample < index and index <= idealpower:
				sample = index
				voltagein = datafinish[k, 0]

		#if 全部見つからなかった場合...
		if voltagein == 0:
			voltagein = 10

		duty = 250/(2.5 + voltagein)    #duty*100 => arduino/100 because 1byte sending.

		print ("No.3")
		print (str(duty))
		time.sleep(3)
		return (duty)

import numpy as np
from math import floor
from math import ceil
import time
import serial
import os
import shutil

#content function import from superclass.
def content(voltage, current, power, idealpower):

	dutymeasure = CalculateDuty()  #made instance

	array = np.array([voltage, current, power])
	multivalue = dutymeasure.dutycalculation1(array, idealpower)

	if multivalue != idealpower:
		idealpower2 = np.round(idealpower, 2)
		multivalue = dutymeasure.dutycalculation2(array, idealpower2)

	if multivalue != idealpower and multivalue != idealpower2:
		idealpower3 = np.round(idealpower, 1)   #電力値により変更あり
		multivalue = dutymeasure.dutycalculation3(array, ,idealpower, idealpower3)

	senddutyvalue = int(multivalue)
	print (senddutyvalue)
	return(senddutyvalue)


# gragh 表示,保存するためのメソッド
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

  os.chdir("/home/ienaga/デスクトップ/python_class_sample/gragh") #change directly

  plt.savefig('sample.png')

  #text file calculate finish

  dailytime = datetime.datetime.now()
  newname = "{0:%Y-%m-%d-%H-%M:%S}.png".format(dailytime)
  os.rename("sample.png",newname)

  os.remove('sample.txt')
