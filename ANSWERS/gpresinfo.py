import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_gpresinfo import Ui_PresInfo

from president_sqlite import President

class PresInfoMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_PresInfo()
        self.ui.setupUi(self)

        # Connect up menu actions
        self.ui.actionQuit.triggered.connect(self.close)

        # Connect up the buttons.
        self.ui.btGetInfo.clicked.connect(self._get_info)

    def _get_info(self):
        term_num = int(self.ui.leTermNum.text())
        p = President(term_num)
        name = f'{p.first_name} {p.last_name}\n'
        birth_location = f'{p.birth_place}, {p.birth_state}\n'
        birth = f'Born: {p.birth_date}\n'
        death = f'Died: {p.death_date}\n'
        served = f'Served: {p.term_start} to {p.term_end}\n'
        party = f'{p.party}\n'
        self.ui.pteInfo.clear()
        for field in name, birth_location, birth, death, served, party:
            self.ui.pteInfo.insertPlainText(field)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = PresInfoMain()
    main.show()
    sys.exit(app.exec_())
