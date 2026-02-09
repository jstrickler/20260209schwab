#!/usr/bin/env python
import sys
import os


from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QColorDialog, QErrorMessage, QInputDialog
from PyQt5.QtGui import QColor

from ui_standard_dialogs import Ui_StandardDialogs

class StandardDialogsMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_StandardDialogs()
        self.ui.setupUi(self)

        self.ui.actionQuit.triggered.connect(lambda:self.close())

        # Connect up the buttons.
        self.ui.btFile.clicked.connect(self._choose_file)  # setup buttons to invoke builtin dialogs
        self.ui.btColor.clicked.connect(self._choose_color)
        self.ui.btMessage.clicked.connect(self._show_error)
        self.ui.btInput.clicked.connect(self._get_input)
           # self.ui.BUTTON_NAME.clicked.connect(self._pushed)

    def _choose_file(self):
        full_path, _ = QFileDialog.getOpenFileName(self, 'Open file', os.getcwd()) # invoke open-file dialog (starts in current directory); returns tuple of selected file path and an empty string
        file_name = os.path.basename(full_path)
        self.ui.statusbar.showMessage("You chose: " + file_name) # update statusbar with chosen filename

    def _choose_color(self):
        result = QColorDialog.getColor() # invoke color selector dialog and return result
        self.ui.statusbar.showMessage(
            "You chose #{0:02x}{1:02x}{2:02x} ({0},{1},{2})".format(
                result.red(),  # result has methods to retrieve color values
                result.green(),
                result.blue()
            )
        )


    def _show_error(self):
        em = QErrorMessage(self)  # invoke error message dialog with specified message
        em.showMessage("There is a problem")
        self.ui.statusbar.showMessage('Diplaying Error')

    def _get_input(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog',
            'Enter your name:')  # invoke input dialog with prompt; returns entered text and boolean flag -- True if user pressed OK, False if user pressed Cancel
        if ok:
            self.ui.statusbar.showMessage("Your name is " + text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = StandardDialogsMain()
    main.show()
    sys.exit(app.exec_())

