import sys, sqlite3
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Database():
    def __init__(self):
        self.con = sqlite3.connect('pythonDB/library.db')
        self.cursor = self.con.cursor()

    def get_all_books(self, available_only, sort_ind):
        query = 'select B.isbn, B.title, B.author, B.genre from Books B'
        if available_only:
            query += ' where B.available=1'
        if sort_ind == 1:
            query += ' order by B.title ASC'
        elif sort_ind == 1:
            query += ' order by B.title DESC'
        self.cursor.execute(query)
        return self.cursor.fetchall()

class Homepage(QMainWindow):
    def __init__(self):
        super().__init__()
        #show login dialog
        # if member
        uic.loadUi('MemberView.ui', self)
        self.member_widget_interactions()
        # else 
            #uic.loadUi('LibrarianView.ui', self)
            #self.librarian_widget_interactions()
        self.database = Database()
        self.populate_table()

    def member_widget_interactions(self):
        self.home_bt.clicked.connect(self.show_home_page)
        self.profile_bt.clicked.connect(self.show_profile_page)
    
    def librarian_widget_interactions(self):
        self.check_in_bt.clicked.connect(self.check_in_book)
        self.check_out_bt.clicked.connect(self.check_out_book)
        self.new_account_bt.clicked.connect(self.create_new_account)
    
    def populate_table(self):
        books = self.database.get_all_books(self.available_books_cb.isChecked(), self.sort_combo.currentIndex())
        for book in books:
            print(book)
            row = self.tableWidget.rowCount()
            for i in range(0, 4):
                self.tableWidget.setItem(row, i, QTableWidgetItem(book[i]))

    def show_home_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def show_profile_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def check_in_book(self):
        pass

    def check_out_book(self):
        pass

    def create_new_account(self):
        pass

app = QApplication(sys.argv)
# member gets MemberHomepage
# librarian/admin get LibrarianHomepage
window = Homepage()
window.show()
sys.exit(app.exec_())