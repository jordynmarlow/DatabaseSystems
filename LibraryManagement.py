import sys, sqlite3
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Database():
    def __init__(self):
        con = sqlite3.connect('')

class LibrarianHomepage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('LibrarianView.ui', self)
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

class MemberHomepage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('MemberView.ui', self)
        self.widget_interactions()

    def widget_interactions(self):
        self.home_bt.clicked.connect(self.show_home_page)
        self.profile_bt.clicked.connect(self.show_profile_page)

    def show_home_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def show_profile_page(self):
        self.stackedWidget.setCurrentIndex(1)

app = QApplication(sys.argv)
# member gets MemberHomepage
# librarian/admin get LibrarianHomepage
window = MemberHomepage()
window.show()
sys.exit(app.exec_())