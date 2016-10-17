import sys
import op
from PySide.QtCore import *
from PySide.QtGui import *
import pyqtgragh as pg

class MainWindow(QWidget):

    # MainWindowクラスの初期化(GUIの生成、シグナルスロット接続)
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
