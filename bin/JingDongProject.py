# -*- coding=gbk -*-
# @author   : aoteman
# @time     : 2022/10/8 21:12

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *    # ����PyQt5����
from PyQt5.QtWidgets import QMainWindow, QApplication,QLabel,QTableWidgetItem,QPushButton,QLineEdit,QGridLayout,QWidget,QTableWidget

from core.UI.Start import Ui_Dialog

class Window(QDialog,Ui_Dialog): # ʵ������ʼ����
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def setup_ui(self):
        pass


class jing_dong_project:
    def __init__(self):
        app = QApplication([])

        window = Window()
        window.show()
        app.exec_()