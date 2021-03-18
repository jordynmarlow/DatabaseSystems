import sys, sqlite3
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Homepage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('LibraryManagement.ui', self)
        self.widget_interactions()

    def widget_interactions(self):
        self.check_in_bt.clicked.connect(self.check_in_book)
        self.check_out_bt.clicked.connect(self.check_out_book)
        self.new_account_bt.clicked.connect(self.create_new_account)

    def check_in_book(self):
        pass

    def check_out_book(self):
        pass

    def create_new_account(self):
        pass

app = QApplication(sys.argv)
window = Homepage()
window.show()
sys.exit(app.exec_())