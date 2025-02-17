# Form implementation generated from reading ui file 'forms.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import sqlite3

class Bookstore:
    def __init__(self, db_name='bookstore.db'):
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        conn = sqlite3.connect(self.db_name)
        conn.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def add_books(self):
        conn = sqlite3.connect(self.db_name)
        conn.executemany('''
            INSERT OR IGNORE INTO books (title, author, price) VALUES (?, ?, ?)
        ''', [
            ('The Great Gatsby', 'F. Scott Fitzgerald', 10.99),
            ('To Kill a Mockingbird', 'Harper Lee', 7.99),
            ('1984', 'George Orwell', 6.99),
            ('Pride and Prejudice', 'Jane Austen', 8.99),
            ('Moby-Dick', 'Herman Melville', 11.99),
            ('The Catcher in the Rye', 'J.D. Salinger', 9.99),
            ('The Hobbit', 'J.R.R. Tolkien', 12.99),
            ('Harry Potter and the Sorcerer\'s Stone', 'J.K. Rowling', 14.99)
        ])
        conn.commit()
        conn.close()

    def find_price(self, title):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.execute("SELECT price FROM books WHERE title = ?", (title,))
        price = cursor.fetchone()
        conn.close()
        return price[0] if price else None

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setStyleSheet("background-color: #f0f0f0;")

        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")

        self.title_label = QtWidgets.QLabel(parent=Form)
        self.title_label.setObjectName("title_label")
        self.title_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        self.verticalLayout.addWidget(self.title_label)

        self.title_input = QtWidgets.QLineEdit(parent=Form)
        self.title_input.setObjectName("title_input")
        self.title_input.setStyleSheet("padding: 5px;")
        self.verticalLayout.addWidget(self.title_input)

        self.price_label = QtWidgets.QLabel(parent=Form)
        self.price_label.setObjectName("price_label")
        self.price_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        self.verticalLayout.addWidget(self.price_label)

        self.price_input = QtWidgets.QLineEdit(parent=Form)
        self.price_input.setObjectName("price_input")
        self.price_input.setStyleSheet("padding: 5px;")
        self.verticalLayout.addWidget(self.price_input)

        self.find_price_button = QtWidgets.QPushButton(parent=Form)
        self.find_price_button.setObjectName("find_price_button")
        self.find_price_button.setStyleSheet("padding: 5px; background-color: #4CAF50; color: white; border: none;")
        self.verticalLayout.addWidget(self.find_price_button)

        self.quantity_label = QtWidgets.QLabel(parent=Form)
        self.quantity_label.setObjectName("quantity_label")
        self.quantity_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        self.verticalLayout.addWidget(self.quantity_label)

        self.quantity_input = QtWidgets.QLineEdit(parent=Form)
        self.quantity_input.setObjectName("quantity_input")
        self.quantity_input.setStyleSheet("padding: 5px;")
        self.verticalLayout.addWidget(self.quantity_input)

        self.total_label = QtWidgets.QLabel(parent=Form)
        self.total_label.setObjectName("total_label")
        self.total_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        self.verticalLayout.addWidget(self.total_label)

        self.total_input = QtWidgets.QLineEdit(parent=Form)
        self.total_input.setObjectName("total_input")
        self.total_input.setStyleSheet("padding: 5px;")
        self.verticalLayout.addWidget(self.total_input)

        self.find_total_button = QtWidgets.QPushButton(parent=Form)
        self.find_total_button.setObjectName("find_total_button")
        self.find_total_button.setStyleSheet("padding: 5px; background-color: #4CAF50; color: white; border: none;")
        self.verticalLayout.addWidget(self.find_total_button)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        
        self.find_price_button.clicked.connect(self.on_find_price_button_clicked)
        self.find_total_button.clicked.connect(self.on_find_total_button_clicked)

      
        self.bookstore = Bookstore()
        self.bookstore.add_books()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Book Store App"))
        self.title_label.setText(_translate("Form", "Book Title:"))
        self.price_label.setText(_translate("Form", "Price:"))
        self.find_price_button.setText(_translate("Form", "Find Price"))
        self.quantity_label.setText(_translate("Form", "Quantity:"))
        self.total_label.setText(_translate("Form", "Total:"))
        self.find_total_button.setText(_translate("Form", "Find Total Amount"))

    def on_find_price_button_clicked(self):
        title = self.title_input.text()
        price = self.bookstore.find_price(title)
        if price:
            self.price_input.setText(str(price))
        else:
            self.price_input.setText("Book not found")

    def on_find_total_button_clicked(self):
        try:
            price = float(self.price_input.text())
            quantity = int(self.quantity_input.text())
            total = price * quantity
            self.total_input.setText(str(total))
        except ValueError:
            self.total_input.setText("Invalid input")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
