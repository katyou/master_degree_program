import sys
import os
from PyQt4.QtGui import *
from PyQt4 import QtGui
import datetime

class MainWindow(QMainWindow):

    # MainWindowクラスの初期化(GUIの生成、シグナルスロット接続)
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(50, 50, 800, 700)
        self.setWindowTitle('LineEdit')

        self.textbox = QLineEdit(self)
        self.textbox.move(10,10)
        self.textbox.resize(140,20)
        self.show()

        # timer = QTimer(self)
        # timer.timeout.connect(self.time_draw)
        # timer.start(1000) #msec

    def time_draw(self):
        d = datetime.datetime.today()
        daystr=d.strftime("%Y-%m-%d %H:%M:%S")
        self.statusBar().showMessage(daystr)
        self.textbox.setText(daystr)



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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # ウィンドウを作成して表示する
    mainWin = MainWindow()
    sys.exit(app.exec_())
