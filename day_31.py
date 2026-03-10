import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout

app = QApplication(sys.argv)

window = QWidget()
window.resize(300, 300)

text = QTextEdit(window)

layout = QVBoxLayout()
layout.addWidget(text)
window.setLayout(layout)

window.show()
sys.exit(app.exec_())

#########################################################
#########################################################

# login page

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

def login():
    user = username.text()
    pswd = password.text()
    if user == "admin" and pswd == "123":
        result.setText("Login successful")
    else:
        result.setText("Invalid credentials")

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Login Form")
window.resize(300, 300)

username = QLineEdit(window)
username.setPlaceholderText("Enter username")
password = QLineEdit(window)
password.setPlaceholderText("Enter password")
button = QPushButton("Login")
result = QLabel("", window)

layout = QVBoxLayout()
layout.addWidget(username)
layout.addWidget(password)
layout.addWidget(button)
layout.addWidget(result)
window.setLayout(layout)

button.clicked.connect(login)

window.show()
sys.exit(app.exec_())


#########################################################
#########################################################

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt # for alignment, works with QVBoxLayout only
from PyQt5.QtGui import QFont

app = QApplication(sys.argv)

window = QWidget()
window.setStyleSheet("background-color:lightblue")
# window.resize(300, 300)

label = QLabel("Hello from PyQt", window)
label.setAlignment(Qt.AlignCenter)
label.setFont(QFont('Ariel', 14))
label.setStyleSheet("color:red; background-color:green")

layout = QVBoxLayout()
layout.addWidget(label)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())


######################################################
######################################################
######################################################
######################################################

print("Task 1: create a dictionary for products and prices\n")
products = {"laptop": 75000, "mouse": 450, "keyboard": 1900, "monitor": 2500}
item = input("enter the item name: ")
if item in products:
    print(f"original price of {item} is: ", products[item])
    price = int(input("enter the updated price: "))
    products[item] = price
else:
    print("product does not exist")
print(products.items())

print("=============================================")
######################################################
######################################################

print("Task 2: Menu based RGB Color Codes\n")

r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)

while True:
    print("1. Red")
    print("2. Green")
    print("3. Blue")
    print("4. Exit")
    c = int(input("Enter your choice: "))
    if c == 1:
        print("RGB code for Red is:", r)
    elif c == 2:
        print("RGB code for Green is:", g)
    elif c == 3:
        print("RGB code for Blue is:", b)
    elif c == 4:
        print("Exiting program")
        break
    else:
        print("Invalid choice")

print("=============================================")
######################################################
######################################################

print("Task 3: Social media followers comparision\n")

i1_fol = {"Alice", "Bob", "Charlie", "David", "eva"}
i2_fol = {"Charlie", "David", "Frank", "George", "Alice"}

print("Mutual followers are: ", i1_fol.intersection(i2_fol))

print("All followers are: ", i1_fol.union(i2_fol))

fol = set()
for i in i1_fol:
    if i not in i2_fol:
        fol.add(i)
for i in i2_fol:
    if i not in i1_fol:
        fol.add(i)

print("Followers following only 1 influencer are: ", fol)

'''
1. Display Text in a Window
Task: Create a window that displays the text “Hello [Your Name]” in the center.

2. Button Click Message
Task: Create a button. When the button is clicked, display “Button Clicked”.

3. Simple Addition Calculator
Task: Enter two numbers and display their sum.

4. Change Background Color
Task: Create a button that changes the background color of the window.

5. Create a counter app (increase number when button clicked)

6. Create a dropdown menu with 5 languages

7. Create a student registration form

'''



import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Task 1: Display Text in a Window")
window.resize(300, 300)
window.setStyleSheet("background-color:lightblue")

label = QLabel("Hello Abdul", window)
label.setAlignment(Qt.AlignCenter)
label.setFont(QFont('Ariel', 14))
label.setStyleSheet("color:red; background-color:green")

layout = QVBoxLayout()
layout.addWidget(label)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())

#####################################################
#####################################################


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

def click():
    result.setText("Button Clicked!!")

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Task 2: Button Click Message")
window.resize(300, 300)

button = QPushButton("Click the button")
result = QLabel("", window)
result.setAlignment(Qt.AlignCenter)
result.setFont(QFont('Ariel', 14))

layout = QVBoxLayout()
layout.addWidget(button)
layout.addWidget(result)
window.setLayout(layout)

button.clicked.connect(click)

window.show()
sys.exit(app.exec_())

#####################################################
#####################################################

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

def add():
    num1 = int(b.text())
    num2 = int(d.text())
    f.setText(str(num1 + num2))

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Task 3: Simple Addition Calculator")
window.resize(300, 300)

a = QLabel("Enter first number: ", window)
b = QLineEdit()
c = QLabel("Enter second number: ", window)
d = QLineEdit()
e = QPushButton("Add", window)
f = QLabel("", window)

layout = QVBoxLayout()
layout.addWidget(a)
layout.addWidget(b)
layout.addWidget(c)
layout.addWidget(d)
layout.addWidget(e)
layout.addWidget(f)

window.setLayout(layout)
e.clicked.connect(add)
window.show()
sys.exit(app.exec_())

#####################################################
#####################################################

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

def change():
    window.setStyleSheet("background-color:grey")

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Task 4: Change Background Color")
window.setStyleSheet("background-color:lightblue")
window.resize(300, 300)

button = QPushButton("Change Background")

layout = QVBoxLayout()
layout.addWidget(button)
window.setLayout(layout)
button.clicked.connect(change)
window.show()
sys.exit(app.exec_())

#####################################################
#####################################################

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

def click():
    n = int(result.text())
    result.setText(str(n+1))


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Task 5: counter app")
window.resize(300, 300)

button = QPushButton("Click to count")
result = QLabel("0", window)
result.setAlignment(Qt.AlignCenter)
result.setFont(QFont('Ariel', 14))

layout = QVBoxLayout()
layout.addWidget(button)
layout.addWidget(result)
window.setLayout(layout)

button.clicked.connect(click)

window.show()
sys.exit(app.exec_())

#####################################################
#####################################################

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QVBoxLayout, QLabel

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Task 6: dropdown menu")
window.resize(300, 200)

label = QLabel("Select a language", window)
combo = QComboBox()
combo.addItem("Python")
combo.addItem("JAVA")
combo.addItem("C++")
combo.addItem("HTML")
combo.addItem("JavaScript")

layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(combo)

window.setLayout(layout)

window.show()
sys.exit(app.exec_())

#####################################################
#####################################################

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

def reg():
    a = name.text()
    b = usn.text()
    c = intern.text()
    if a == "" or b == "" or c == "":
        result.setText("Fill every cells to register!!")
    else:
        result.setText("Registration Successfull!!")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Task 7: Student Registration Form")
window.resize(300, 300)
name = QLineEdit(window)
name.setPlaceholderText("Enter Student Name")
usn = QLineEdit(window)
usn.setPlaceholderText("Enter Student USN")
intern = QLineEdit(window)
intern.setPlaceholderText("Enter Internship Company")
button = QPushButton("Register")
result = QLabel("", window)
result.setAlignment(Qt.AlignCenter)
result.setFont(QFont('Ariel', 14))
layout = QVBoxLayout()
layout.addWidget(name)
layout.addWidget(usn)
layout.addWidget(intern)
layout.addWidget(button)
layout.addWidget(result)
window.setLayout(layout)
button.clicked.connect(reg)
window.show()
sys.exit(app.exec_())


