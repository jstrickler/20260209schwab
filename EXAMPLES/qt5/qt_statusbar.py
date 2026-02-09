#!/usr/bin/env python
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from statusbar_ui import Ui_StatusBar

class StatusBarMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self._count = 0

        # Setup the user interface from Designer.
        self.ui = Ui_StatusBar()
        self.ui.setupUi(self)

        self.ui.btPushMe.clicked.connect(self._pushed)
        self.ui.btPullYou.clicked.connect(self._pulled)
        self._update_statusbar(0) # do initial status bar update

    def _pushed(self, ev):
        self._update_statusbar(1)

    def _pulled(self, ev):
        self._update_statusbar(-1)

    def _update_statusbar(self, value):
        self._count += value
        msg = "Count is " + str(self._count)
        self.ui.statusbar.showMessage(msg, 0) # show message, 0 means no timeout, >= 0 means timeout in seconds


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = StatusBarMain()
    main.show()
    app.exec()


