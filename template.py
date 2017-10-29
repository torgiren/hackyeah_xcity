# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(577, 442)
        self.start_button = QtGui.QPushButton(Form)
        self.start_button.setEnabled(False)
        self.start_button.setGeometry(QtCore.QRect(340, 288, 201, 61))
        self.start_button.setObjectName(_fromUtf8("start_button"))
        self.combo_ulica = QtGui.QComboBox(Form)
        self.combo_ulica.setEnabled(False)
        self.combo_ulica.setGeometry(QtCore.QRect(340, 208, 201, 31))
        self.combo_ulica.setObjectName(_fromUtf8("combo_ulica"))
        self.combo_numer = QtGui.QComboBox(Form)
        self.combo_numer.setEnabled(False)
        self.combo_numer.setGeometry(QtCore.QRect(340, 248, 201, 31))
        self.combo_numer.setObjectName(_fromUtf8("combo_numer"))
        self.label_ulica = QtGui.QLabel(Form)
        self.label_ulica.setGeometry(QtCore.QRect(172, 212, 160, 20))
        self.label_ulica.setObjectName(_fromUtf8("label_ulica"))
        self.label_numer = QtGui.QLabel(Form)
        self.label_numer.setGeometry(QtCore.QRect(140, 251, 201, 21))
        self.label_numer.setObjectName(_fromUtf8("label_numer"))
        self.label_ulica_2 = QtGui.QLabel(Form)
        self.label_ulica_2.setGeometry(QtCore.QRect(270, 50, 161, 30))
        self.label_ulica_2.setObjectName(_fromUtf8("label_ulica_2"))
        self.input_button = QtGui.QPushButton(Form)
        self.input_button.setGeometry(QtCore.QRect(430, 50, 110, 31))
        self.input_button.setObjectName(_fromUtf8("input_button"))
        self.label_ulica_3 = QtGui.QLabel(Form)
        self.label_ulica_3.setGeometry(QtCore.QRect(244, 116, 181, 30))
        self.label_ulica_3.setObjectName(_fromUtf8("label_ulica_3"))
        self.slownik_button = QtGui.QPushButton(Form)
        self.slownik_button.setGeometry(QtCore.QRect(430, 115, 111, 31))
        self.slownik_button.setObjectName(_fromUtf8("slownik_button"))
        self.input_path = QtGui.QPlainTextEdit(Form)
        self.input_path.setEnabled(False)
        self.input_path.setGeometry(QtCore.QRect(20, 81, 521, 31))
        self.input_path.setMaximumSize(QtCore.QSize(16777215, 31))
        self.input_path.setObjectName(_fromUtf8("input_path"))
        self.slownik_path = QtGui.QPlainTextEdit(Form)
        self.slownik_path.setEnabled(False)
        self.slownik_path.setGeometry(QtCore.QRect(20, 150, 521, 31))
        self.slownik_path.setMaximumSize(QtCore.QSize(16777215, 31))
        self.slownik_path.setObjectName(_fromUtf8("slownik_path"))
        self.pushButton_exit = QtGui.QPushButton(Form)
        self.pushButton_exit.setGeometry(QtCore.QRect(340, 360, 201, 61))
        self.pushButton_exit.setObjectName(_fromUtf8("pushButton_exit"))
        self.label_status = QtGui.QLabel(Form)
        self.label_status.setGeometry(QtCore.QRect(50, 310, 271, 20))
        self.label_status.setText(_fromUtf8(""))
        self.label_status.setObjectName(_fromUtf8("label_status"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.start_button.setText(_translate("Form", "Start", None))
        self.label_ulica.setText(_translate("Form", "Wybierz kolumnę z ulicą:", None))
        self.label_numer.setText(_translate("Form", "Wybierz kolumne z numerem:", None))
        self.label_ulica_2.setText(_translate("Form", "Wybierz plik wejściowy:", None))
        self.input_button.setText(_translate("Form", "Przeglądaj", None))
        self.label_ulica_3.setText(_translate("Form", "Wybierz plik ze słownikiem:", None))
        self.slownik_button.setText(_translate("Form", "Przeglądaj", None))
        self.pushButton_exit.setText(_translate("Form", "Exit", None))

