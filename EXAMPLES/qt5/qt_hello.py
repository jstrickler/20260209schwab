#!/usr/bin/env python
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel # Standard PyQt5 imports

class HelloWindow(QMainWindow): # Main class inherits from QMainWindow to have normal application behavior

    def __init__(self):
        super().__init__()
        self._label = QLabel("Hello PyQt5 World")
        self.setCentralWidget(self._label)

if __name__ == "__main__":
    app = QApplication(sys.argv)  # These 4 lines are always required. Only the name of the main window object changes.
    main_window = HelloWindow()
    main_window.show()
    sys.exit(app.exec_())
