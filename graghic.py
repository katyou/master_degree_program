# coding:UTF-8

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui
import PyQt4.QtCore as QtCore
import datetime

class MainWindow(QMainWindow):

    # MainWindowクラスの初期化(GUIの生成、シグナルスロット接続)
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    #view component 追加
    def initUI(self):
        self.setGeometry(50, 50, 800, 700)
        self.setWindowTitle('太陽電池測定ソフト')

        #時刻付きlabel追加
        self.textbox = QLineEdit(self)
        self.textbox.move(10,10)
        self.textbox.resize(250,30)
        timer = QTimer(self)
        timer.timeout.connect(self.time_draw)
        timer.start(10)

        #label追加
        self.label1 = QLabel('Duty値', self)
        self.label1.setGeometry(600,500,100,100)
        self.label1.resize(200,200)

        self.label2 = QLabel('ここにduty値が来るようにする', self)
        self.label2.setGeometry(600,520,200,200)
        #self.label2.setPointSize(32)

        button = QtGui.QPushButton('測定スタート',self)
        button.setGeometry(550,200,200,100)
        #self.connect(button, QtCore.SIGNAL('clicked()'), self.filename)

        button = QtGui.QPushButton('FINISH',self)
        button.setGeometry(550,300,200,50)
        #self.connect(button, QtCore.SIGNAL('clicked()'), self.filename)

        comment = "測定装置停止中"
        self.label = QLabel(comment, self)
        self.label.setGeometry(600,10,150,50)
        #self.label.resize(200,200)

        self.show()

    def time_draw(self):
        d = datetime.datetime.today()
        daystr = d.strftime("20%y年%m月%d日 %H時%M分%S秒")
        daystring = d.strftime("%m月%d日 %H時%M分")
        self.statusBar().showMessage(daystring)
        self.textbox.setText(daystr)

    def comment(answer):
        print("how")



# [5]
    # fileNameListWidgetを更新する
    def updateFileNameListWidget(self, fileNameListWidget, folderPath):
        print('updateFileNameListWidget')

# [6]
    # グラフ生成関数
    def createGraph(self, folderPath, fileName):
        print('createGraph')

# [6.1]
    # データリストの集合を生成する
    def createDataListSet(self, folderPath, fileName):
        print('createDataListSet')

# [6.2]
    # データリストの集合を読み込む
    def loadDataListSet(self, folderPath, fileName):
        print('loadDataListSet')

# [6.3]
    # テスト用グラフを生成する
    def createTestGraph(self, dataListSet):
        print('createTestGraph')

# [6.4]
    #スタートボタン押下時
    def clickedstart(self, filename):
        print("start")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # ウィンドウを作成して表示する
    mainWin = MainWindow()
    sys.exit(app.exec_())
