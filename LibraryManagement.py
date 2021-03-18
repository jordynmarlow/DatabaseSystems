# jordyn
import sys, sqlite3, datetime
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Database():
    def __init__(self):
        self.con = sqlite3.connect('pythonDB/library.db')
        self.cursor = self.con.cursor()

    def get_all_books(self, available_only, sort_ind, keyword):
        query = 'select B.isbn, B.title, B.author, B.genre, B.bid from Books B'
        if available_only:
            query += ' where B.available=1'
        if sort_ind == 1:
            query += ' order by B.title ASC'
        elif sort_ind == 1:
            query += ' order by B.title DESC'
        if len(keyword) > 0:
            query = "select * from (%s) where (isbn like '%s' or title like '%s' or author like\
                 '%s' or genre like '%s')" % (query, keyword, keyword, keyword, keyword)
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def check_credentials(self, username, password):
        self.cursor.execute('select password from users where username=\'%s\'' % username)
        result = self.cursor.fetchall()[0][0]
        if result == []:
            return False
        elif result == password:
            return True
        
    def create_account(self, u, p, t, n, e):
        # change to fit users schema
        self.cursor.execute('insert into users (username, password, type, name, email)\
             VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' % (u, p, t, n, e))

    def check_in_book(self, bid):
        self.cursor.execute('delete from checkedOut where bid=%d' % int(bid))
        self.cursor.execute('update books set available=1 where bid=\'%s\'' % bid)
    
    def check_out_book(self, bid, username):
        due_date = str(datetime.datetime.today() + datetime.timedelta(days=14))[:10]
        self.cursor.execute('insert into checkedOut (bid, username, dueDate) values (%d, \'%s\', \'%s\')' % (int(bid), username, due_date))
        self.cursor.execute('update books set available=0 where bid=\'%s\'' % bid)
    
    def get_user_type(self, username):
        self.cursor.execute('select type from users where username=\'%s\'' % username)
        return self.cursor.fetchall()[0][0]
    
    def delete_book(self, bid):
        self.cursor.execute('delete from books where bid=%d' % int(bid))

    def add_book(self, t, a, g, y, i, b):
        self.cursor.execute('insert into books (title, author, genre, year, available, isbn, bd) values\
             (\'%s\', \'%s\', \'%s\', %d, 1, %d, %d)' % (t, a, g, y, i, b))
    
class CheckOutBook(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('CheckOutDialog.ui', self)
        self.check_out_bt.clicked.connect(self.check_out_book)

    def check_out_book(self):
        database.check_out_book(self.bid_le.text(), self.username_le.text())
        self.close()

class LoginPage(QDialog):
    def __init__(self, homepage):
        super().__init__()
        uic.loadUi('LoginDialog.ui', self)
        self.sign_in_bt.clicked.connect(self.sign_in)
        self.warning_lbl.hide()
        self.valid = False
        self.homepage = homepage

    def closeEvent(self, event):
        if not self.valid:
            sys.exit(app.exec_())

    def sign_in(self):
        self.valid = database.check_credentials(self.username_le.text(), self.password_le.text())
        if self.valid:
            self.homepage.username = self.username_le.text()
            self.close()
        else:
            self.warning_lbl.show()

class CreateAccount(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('NewAccountDialog.ui', self)
        self.create_user_bt.clicked.connect(self.new_account)
    
    def new_account(self):
        u = self.username_le.text()
        p = self.password_le.text()
        t = self.type_combo.currentText()
        n = self.name_le.text()
        e = self.email_le.text()
        database.create_account(u, p, t, n, e)
        self.close()

class AddBook(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('NewBookDialog.ui', self)
        self.create_book_bt.clicked.connect(self.create_book)

    def create_book(self):
        database.add_book()

class Homepage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sign_in()
    
    def sign_in(self):
        self.hide()
        login_page = LoginPage(self)
        login_page.exec_()
        user_type = database.get_user_type(self.username)
        if user_type == 'Member':
            uic.loadUi('MemberView.ui', self)
            self.member_widget_interactions()
        else: 
            uic.loadUi('LibrarianView.ui', self)
            self.librarian_widget_interactions()
            if user_type == 'Librarian':
                self.new_account_bt.hide()
                self.add_book_bt.hide()
                self.delete_book_bt.hide()
        self.widget_interactions()
        self.populate_table()
        self.show()
    
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Exit', 'Are you sure you want to exit? You will be signed out.',\
             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            database.cursor.close()
            database.con.commit()
            event.accept()
        else:
            event.ignore()
    
    def widget_interactions(self):
        self.search_bt.clicked.connect(self.populate_table)
        self.sign_out_bt.clicked.connect(self.sign_in)

    def member_widget_interactions(self):
        self.home_bt.clicked.connect(self.show_home_page)
        self.profile_bt.clicked.connect(self.show_profile_page)
    
    def librarian_widget_interactions(self):
        self.check_in_bt.clicked.connect(self.check_in_book)
        self.check_out_bt.clicked.connect(self.check_out_book)
        self.new_account_bt.clicked.connect(self.create_new_account)
        self.add_book_bt.clicked.connect(self.add_book)
        self.delete_book_bt.clicked.connect(self.delete_book)
    
    def populate_table(self):
        self.tableWidget.setRowCount(0)
        books = database.get_all_books(self.available_books_cb.isChecked(), self.sort_combo.currentIndex(), self.search_bar.text())
        for i in range(0, len(books)):
            self.tableWidget.insertRow(i)
            for j in range(0, 5):
                item = QTableWidgetItem(str(books[i][j]))
                item.setFlags(Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, j, item)

    def show_home_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def show_profile_page(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def add_book(self):
        pass

    def delete_book(self):
        bid, ok = QInputDialog.getText(self, 'Delete book', 'Enter the book ID number: ')
        if ok:
            database.delete_book(bid)

    def check_in_book(self):
        bid, ok = QInputDialog.getText(self, 'Check in book', 'Enter the book ID number: ')
        if ok:
            database.check_in_book(bid)

    def check_out_book(self):
        dlg = CheckOutBook()
        dlg.exec_()

    def create_new_account(self):
        dlg = CreateAccount()
        dlg.exec_()

app = QApplication(sys.argv)
database = Database()
window = Homepage()
window.show()
sys.exit(app.exec_())