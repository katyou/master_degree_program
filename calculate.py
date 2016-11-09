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

			if index == 2.708:     #取り出したい電力の値 part1
				voltagein = data[x, 0]
				duty = 2.9/(2.9 + voltagein)
				#sendingvalue = duty * 1023
				print ("No.1")
				print (str(duty))
				time.sleep(5)
				return (duty)
				break

			else:
				x += 1
		#return (index)

	def dutycalculation2(self, a):
		import numpy as np
		nextvalue = np.round(a, 1)
		datathree = np.transpose(nextvalue)
		sample = open("test2.txt", "w")
		sample.write(str(datathree))
		sample.close()

		for z in range (1, 299):
			index = datathree[z, 2]

			if index == 2.71:      #取り出したい電力の値 part 3
				voltagein = datathree[z, 0]
				duty = 2.9/(2.9 + voltagein)
				#sendingvalue = duty * 1023
				print ("No.3")
				print (str(duty))
				time.sleep(5)
				return (duty)
				break
			else:
				z += 1

	def dutycalculation3(self, a):
		import numpy as np
		nextvalue = np.round(a,2)
		datafinish = np.transpose(nextvalue)
		k = 1
		sample = 0

		for k in range (1, 299):
			index = datafinish[k, 2]
			if sample < index and index <= 2.35:
				sample = index
				voltagein = datafinish[k, 0]
			else:
				k += 1

		duty = 2.9/(2.9 + voltagein)
		#sendingvalue = duty * 1023

		print ("No.4")
		print (str(duty))
		return (duty)
		time.sleep(3)


#content function import from superclass.
def content(volta, currenting, powering):
	import numpy as np
	from math import floor
	from math import ceil
	import time
	import serial
	import os
	import shutil
	index = 0

	dutymeasure = CalculateDuty()  #class declare

	a = np.array([volta, currenting, powering])
	support = np.round(a, 3)
	data = np.transpose(support)

	sample = open("test.txt", "w")
	sample.write(str(data))
	sample.close()

	dutymeasure.dutycalculation1(data)

	if index != 2.708:
		dutymeasure.dutycalculation2(a)

	if index != 2.771 and index != 2.77:
		if index != 2.8:
			dutymeasure.dutycalculation3(a)

	senddutyvalue = int(duty)
	dutying = str(duty) + '\r\n'
	print (str(dutying))

	serialconnect = dutymeasure.changeserial()
	ser = serial.Serial(serialconnect, 115200)
	time.sleep(2)

	ser.write(bytes([senddutyvalue]))


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
