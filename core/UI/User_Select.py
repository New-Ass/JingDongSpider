# -*- coding=gbk -*-
# @author   : aoteman
# @time     : 2022/10/8 21:45

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *    # 导入PyQt5部件
from PyQt5.QtWidgets import QMainWindow, QApplication,QLabel,QTableWidgetItem,QPushButton,QLineEdit,QGridLayout,QWidget,QTableWidget


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(619, 464)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(490, 50, 111, 61))
        self.pushButton.clicked.connect(self.run)

        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(60, 50, 391, 61))

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 190, 131, 51))

        self.textEdit_2 = QTextEdit(Dialog)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(210, 190, 271, 41))

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 260, 131, 51))

        self.comboBox = QComboBox(Dialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(220, 270, 111, 31))

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 320, 131, 51))

        self.textEdit_3 = QTextEdit(Dialog)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(210, 330, 341, 31))

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 380, 171, 51))

        self.textEdit_4 = QTextEdit(Dialog)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(210, 390, 341, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u5f00\u59cb\u722c\u53d6", None))
        self.textEdit.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600;\">\u5546\u54c1\u8bc4\u8bba\u722c\u53d6</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u8981\u722c\u53d6\u7684\u5546\u54c1\u540d\u79f0", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u9009\u62e9\u9875\u9762\u6392\u5e8f\u65b9\u5f0f", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"\u7efc\u5408", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"\u9500\u91cf", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"\u8bc4\u8bba\u6570", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"\u65b0\u54c1", None))

        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u8981\u722c\u53d6\u7684\u5546\u54c1\u9875\u6570", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u6700\u597d\u4fdd\u8bc1\u8be5\u5546\u54c1\u9875\u6570 \u5927\u4e8e\u7b49\u4e8e \u586b\u5199\u7684\u9875\u6570</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u8981\u722c\u53d6\u7684\u5546\u54c1\u8bc4\u8bba\u6570\u9875\u6570", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u6700\u597d\u4fdd\u8bc1\u8be5\u5546\u54c1\u9875\u6570 \u5927\u4e8e\u7b49\u4e8e \u586b\u5199\u7684\u9875\u6570</p></body></html>", None))
    # retranslateUi

    def run(self):
        name = self.textEdit_2.toPlainText() # 要爬取的商品名称
        paixu = self.comboBox.currentText() # 页面商品的排序方式
        good_page = self.textEdit_3.toPlainText() # 要爬取的商品页数
        comment_page = self.textEdit_4.toPlainText() # 要爬取的商品评论数页数

        from core.UI.Wait import user_wait_window
        self.window = user_wait_window()
        self.window.show()

        from core.Spider.spider import Spider
        Spider(name, paixu, good_page, comment_page)

class user_selelct_window(QDialog, Ui_Dialog): # 打开用户选择页面
    def __init__(self):
        super().__init__()
        self.setupUi(self)