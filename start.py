#!/usr/bin/env python3
import sys
from PyQt4 import QtCore, QtGui

from template import Ui_Form

#dane od fabryka
def get_data(typ):
    if typ is "backend":
        a = { "nr": 0, "adres": 1, "stan_nawie" : 2}

    if typ is "slownik":
        a = { "nr": 0, "adres": 1, "stan_nawie" : 2}
    return a

def start_prog():
    print("abc")
    

class MyForm(QtGui.QMainWindow):
    def wyszukaj_plik(self,label,typ):
        input_file_path = QtGui.QFileDialog.getOpenFileName()
        label.document().setPlainText(input_file_path)
        
        if typ is "input":
            if input_file_path:
                dane = get_data("backend")
                for item in dane:
                    self.ui.combo_ulica.addItem(item)
            
                for item in dane:
                    self.ui.combo_numer.addItem(item)
                self.ui.combo_ulica.setEnabled(True)
                self.ui.combo_numer.setEnabled(True)
                self.change_input = True
        if typ is "slownik":
            if input_file_path:
                dane = get_data("slownik")
                self.change_slownik = True

        if self.change_slownik is True and self.change_input is True:
            self.ui.start_button.setEnabled(True)
        
        return input_file_path

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.start_button.clicked.connect(start_prog)
        self.ui.input_button.clicked.connect(lambda: self.wyszukaj_plik(self.ui.input_path, "input"))
        self.ui.slownik_button.clicked.connect(lambda: self.wyszukaj_plik(self.ui.slownik_path, "slownik"))
        self.input_file_path = None
        self.change_input = None
        self.change_slownik = None

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.setWindowTitle('X-City - HackYeah - LinuxGods');
    myapp.show()
    sys.exit(app.exec_())
