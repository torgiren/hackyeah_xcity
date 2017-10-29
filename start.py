#!/usr/bin/env python3
import sys
import parse 
from PyQt4 import QtCore, QtGui
from template import Ui_Form

    

class MyForm(QtGui.QMainWindow):
    def wyszukaj_plik(self,label,typ):
        input_file_path = QtGui.QFileDialog.getOpenFileName()
        label.document().setPlainText(input_file_path)
        
        if typ is "input":
            if input_file_path:
                self.input_path = input_file_path
                dane1 = parse.get_headers(input_file_path)
                for item in dane1:
                    self.ui.combo_ulica.addItem(item, dane1[item])
            
                for item in dane1:
                    self.ui.combo_numer.addItem(item, dane1[item])
                self.ui.combo_ulica.setEnabled(True)
                self.ui.combo_numer.setEnabled(True)
                self.change_input = True
        if typ is "slownik":
            if input_file_path:
                self.slownik_path = input_file_path
                dane2 = parse.get_headers(input_file_path)
                self.change_slownik = True

        if self.change_slownik is True and self.change_input is True:
            self.ui.start_button.setEnabled(True)
        
        return input_file_path

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.input_button.clicked.connect(lambda: self.wyszukaj_plik(self.ui.input_path, "input"))
        self.ui.slownik_button.clicked.connect(lambda: self.wyszukaj_plik(self.ui.slownik_path, "slownik"))
        self.ui.combo_ulica.activated.connect(self.onActivated_dane1)
        self.ui.combo_numer.activated.connect(self.onActivated_dane2)
        self.ui.start_button.clicked.connect(self.start_prog)

        self.input_path = None
        self.slownik_path = None
        self.change_input = None
        self.change_slownik = None 
        self.street_col = None
        self.number_col = None
    def onActivated_dane1(self, text):
        self.street_col = self.ui.combo_ulica.itemData(text)
    def onActivated_dane2(self, text):
        self.number_col = self.ui.combo_numer.itemData(text)
    def start_prog(self):
        parse.load_slownik(self.slownik_path)
        parse.load_dane(self.input_path, self.street_col, self.number_col)
        parse.licz() 

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.setWindowTitle('X-City - HackYeah - LinuxGods');
    myapp.show()
    sys.exit(app.exec_())
