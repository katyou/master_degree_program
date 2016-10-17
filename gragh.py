# coding:UTF-8  

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