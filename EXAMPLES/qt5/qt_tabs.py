#!/usr/bin/env python
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_tabs import Ui_Tabs

class TabsMain(QMainWindow):   
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_Tabs()
        self.ui.setupUi(self)

        self.ui.actionQuit.triggered.connect(lambda:self.close())
        self.ui.actionA.triggered.connect(lambda: self._show_tab('A'))
        self.ui.actionB.triggered.connect(lambda: self._show_tab('B'))
        self.ui.actionC.triggered.connect(lambda: self._show_tab('C'))
        
    def _show_tab(self, which_tab):
        if which_tab == 'A':
            self.ui.tabWidget.setCurrentIndex(0)  # choose tab programmatically
            self.ui.labA.setText('Aardvark')  # set text on label widget on tab
        elif which_tab == 'B':
            self.ui.tabWidget.setCurrentIndex(1)  # choose tab programmatically
            self.ui.labB.setText('Bonobo')  # set text on label widget on tab
        elif which_tab == 'C':
            self.ui.tabWidget.setCurrentIndex(2)  # choose tab programmatically
            self.ui.labC.setText('Coatimundi')  # set text on label widget on tab

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TabsMain()
    main.show()
    sys.exit(app.exec_())


