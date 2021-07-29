#/usr/bin/python3
# Creating a login form using PyQt5

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout)
class Loginpage(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle('Login')
    self.resize(350,200)
    layout = QGridLayout()
    label1 = QLabel('<font size="8"> UserId </font>')
    self.user_obj = QLineEdit()
    layout.addWidget(label1, 0, 0)
    layout.addWidget(self.user_obj, 0, 1)
    label2 = QLabel('<font size="8"> Password </font>')
    self.user_pwd = QLineEdit()
    layout.addWidget(label2, 1, 0)
    layout.addWidget(self.user_pwd, 1, 1)
    button_login = QPushButton('Login')
    layout.addWidget(button_login, 2, 0, 2, 2)
    self.setLayout(layout)
app = QApplication(sys.argv)
form = Loginpage()
form.show()
sys.exit(app.exec_())