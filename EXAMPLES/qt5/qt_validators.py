#!/usr/bin/env python

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QRegExpValidator, QIntValidator
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtCore import QRegExp

from ui_validators import Ui_Validators

class ValidatorsMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_Validators()

        self.ui.setupUi(self)
        self._set_validators()

        self.ui.bt_save.clicked.connect(self._save_pushed)

    def _set_validators(self):
        # Set up the validators (could be in separate function or module)
        reg_ex = QRegExp(r"[A-Za-z0-9]{1,10}") # create Qt regular expression object (note use of raw string)
        val_alphanum = QRegExpValidator(reg_ex, self.ui.le_alphanum)  # create regex validator from regex object
        self.ui.le_alphanum.setValidator(val_alphanum) # attach validator to line entry field

        reg_ex = QRegExp(r"[a-z ]{0,30}") # create Qt regular expression object (note use of raw string)
        val_lcspace = QRegExpValidator(reg_ex, self.ui.le_lcspace)  # create regex validator from regex object
        self.ui.le_lcspace.setValidator(val_lcspace) # attach validator to line entry field

        val_nums_1_100 = QIntValidator(1, 100, self.ui.le_nums_1_100)  # create integer validator
        self.ui.le_nums_1_100.setValidator(val_nums_1_100)  # attach validator to line entry field

        val_float = QDoubleValidator(0.0, 20.0, 2, self.ui.le_float)  # create double (large float) validator
        self.ui.le_float.setValidator(val_float)  # attach validator to line entry field

    def _save_pushed(self):
        alphanum = self.ui.le_alphanum.text()
        lcspace = self.ui.le_lcspace.text()
        nums = self.ui.le_nums_1_100.text()
        fl = self.ui.le_float.text()
        msg = '{}/{}/{}/{}'.format(alphanum, lcspace, nums, fl)
        self.ui.statusbar.showMessage(msg, 0) # display valid date on status bar

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ValidatorsMain()
    main.show()
    sys.exit(app.exec_())


