# coding:UTF-8
class CalculateDuty:
	"""Caluculate duty ratio in fuel cell"""

	def __init__(self):
		self.measure = ""

	def dutyratio1(self):
		for i in range (1, 300):
			index = data[x, 2]

			if index == 2.708:     #取り出したい電力の値 part1
				voltagein = data[x, 0]
				duty = 2.9/(2.9 + voltagein)
				sendingvalue = duty * 1023
				print ("No.1")
				print (str(duty))
				time.sleep(5)
				break

			else:
				x += 1

	def dutyratio2(self):
		if index != 2.708 and index != 2.71:
			nextvalue = np.round(a,1)
			datathree = np.transpose(nextvalue)
			z = 0
			sample = open("test2.txt", "w")
			sample.write(str(datathree))
			sample.close()

			for i in range (1, 300):
				index = datathree[z, 2]

				if index == 2.7:       #取り出したい電力の値 part 3
					voltagein = datathree[z,0]
					duty = 2.9/(2.9 + voltagein)
					sendingvalue = duty * 1023
					print ("No.3")
					print (str(duty))
					time.sleep(5)
					break
				else:
					z += 1

	def dutyratio3(self):
		if index != 2.771 and index != 2.77:
			if index != 2.8:
				nextvalue = np.round(a,2)
				datafinish = np.transpose(nextvalue)
				k = 0
				sample = 0

				for i in range (1, 300):
					index = datafinish[k, 2]
					if sample < index and index <= 2.35:
						sample = index
						voltagein = datafinish[k, 0]
					else:
						k += 1

				duty = 2.9/(2.9 + voltagein)
				sendingvalue = duty * 1023

				print ("No.4")
				print (str(duty))
				time.sleep(3)

def content(volta, currenting, powering ):
	import numpy as np
	from math import floor
	from math import ceil
	import time
	dutymeasure = CalculateDuty()  #class declare

	a = np.array([volta, currenting, powering])
	support = np.round(a, 3)
	data = np.transpose(support)

	sample = open("test.txt", "w")
	sample.write(str(data))
	sample.close()
	x = 0

	dutymeasure.dutyratio1()

	dutymeasure.dutyratio2()

	dutymeasure.dutyratio3()


	fusin = int(sendingvalue)
	dutying = str(fusin) + '\r\n'
	print (str(dutying))

	import serial
	import os
	import shutil
	ser = serial.Serial("/dev/ttyACM2", 115200)
	time.sleep(2)

	ser.write(bytes([fusin]))


# gragh 表示,保存するためのメソッド
def graphmodel():
  from matplotlib import pyplot as plt
  import numpy as np
  import time
  import os
  import datetime

  fig = plt.figure()

  plt.xlim([5.5,23])
  plt.ylim([0,0.3])
  plt.plot(voltage, current, '-o')

  s.chdir("/home/ienaga/デスクトップ/python_class_sample/gragh") #change directly

  plt.savefig('sample.png')

  #text file calculate finish

  dailytime = datetime.datetime.now()
  newname = "{0:%Y-%m-%d-%H-%M:%S}.png".format(dailytime)
  os.rename("sample.png",newname)

  os.remove('sample.txt')
