# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JMS_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 480)
        Form.setMinimumSize(QtCore.QSize(800, 480))
        Form.setMaximumSize(QtCore.QSize(800, 480))
        Form.setStyleSheet("")
        self.label_1 = QtWidgets.QLabel(Form)
        self.label_1.setGeometry(QtCore.QRect(490, 75, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Kostar")
        font.setPointSize(16)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.BG_label = QtWidgets.QLabel(Form)
        self.BG_label.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.BG_label.setStyleSheet("background-image: url(:/BG_IMG/BG_IMG.png);")
        self.BG_label.setText("")
        self.BG_label.setObjectName("BG_label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(490, 152, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Kostar")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(490, 230, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Kostar")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(490, 310, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Kostar")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(490, 387, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Kostar")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.BG_label.raise_()
        self.label_1.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_1.setText(_translate("Form", "도란수"))
        self.label_2.setText(_translate("Form", "안녕 친구"))
        self.label_3.setText(_translate("Form", "안녕 친구"))
        self.label_4.setText(_translate("Form", "안녕 친구"))
        self.label_5.setText(_translate("Form", "안녕 친구"))

#import BG_img_rc
