#User Input
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

def greet():
    name = textbox.text()
    result.setText("Hello " + name)

app = QApplication(sys.argv)

window = QWidget()
window.resize(300, 200)

label = QLabel("Enter the name: ", window)
textbox = QLineEdit()
button = QPushButton("Click me", window)
result = QLabel("", window)

layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(textbox)
layout.addWidget(button)
layout.addWidget(result)

window.setLayout(layout)
button.clicked.connect(greet)

window.show()
sys.exit(app.exec_())

##########################################################
##########################################################

#Simple calculation
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

def mul():
    num1 = int(b.text())
    num2 = int(d.text())
    f.setText(str(num1 * num2))

app = QApplication(sys.argv)

window = QWidget()
window.resize(300, 400)

a = QLabel("Enter first number: ", window)
b = QLineEdit()
c = QLabel("Enter second number: ", window)
d = QLineEdit()
e = QPushButton("Multiply", window)
f = QLabel("", window)

layout = QVBoxLayout()
layout.addWidget(a)
layout.addWidget(b)
layout.addWidget(c)
layout.addWidget(d)
layout.addWidget(e)
layout.addWidget(f)

window.setLayout(layout)
e.clicked.connect(mul)
window.show()
sys.exit(app.exec_())

##########################################################
##########################################################

#Simple dropdown

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QVBoxLayout

app = QApplication(sys.argv)

window = QWidget()
window.resize(300, 200)

combo = QComboBox()
combo.addItem("Python")
combo.addItem("JAVA")
combo.addItem("C++")

layout = QVBoxLayout()
layout.addWidget(combo)

window.setLayout(layout)

window.show()
sys.exit(app.exec_())

##########################################################
##########################################################
##########################################################
##########################################################

print("task 1: find the missing number in a sequence")

seq = []
n = int(input("enter the number of terms: "))
for i in range(1, n+1):
    x = int(input(f"enter value {i}: "))
    seq.append(x)

if seq[1] - seq[0] == seq[2] - seq[1]:
    d = seq[1] - seq[0]
    for i in range(len(seq)-1):
        if seq[i] + d == seq[i+1]:
            pass
        else:
            print(f"missing number is: {seq[i]+d}")
else:
    print("the numbers are not in sequence")

print("=======================================================")

print("task 2: check wheather 2 strings are anagrams")
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if sorted(s1) == sorted(s2):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")

print("=======================================================")

print("task 3: Calculate the sum of first n natural numbers")
n = int(input("enter the value for n: "))
sum = 0
for i in range(n+1):
    sum = sum+i
print(sum)

print("=======================================================")

print("task 4: check wheather a number is +ve, -ve or 0")
n = int(input("enter the number: "))
if n>0:
    print("positive number")
elif n<0:
    print("negative number")
else:
    print("number is zero")

print("=======================================================")

print("task 5: sum of digits of a number")
n = int(input("Enter a number: "))
sum = 0
while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10
print("Sum of digits:", sum)

print("=======================================================")

print("task 6: product of digits of a number")
n = int(input("Enter a number: "))
p = 1
while n > 0:
    d = n % 10
    p = p * d
    n = n // 10
print("Product of digits:", p)

print("=======================================================")

print("task 7: LCM of 2 numbers")
a = int(input("enter first number: "))
b = int(input("enter second number: "))
for i in range(1, a*b+1):
    if i % a == 0 and i % b == 0:
        print(f"LCM is: {i}")
        break

print("=======================================================")

print("task 8: GCD of 2 numbers")
a = int(input("enter first number: "))
b = int(input("enter second number: "))
fa = []
fb = []
f = []
for i in range(1, a+1):
    if a%i == 0:
        fa.append(i)
for i in range(1, b+1):
    if b%i == 0:
        fb.append(i)
for i in fa:
    if i in fb:
        f.append(i)
print(f"GCD is: {max(f)}")

print("=======================================================")

print("task 9: Common elements in 2 lists")
l1 = [2, 4, 6, 8, 10, 12, 14, 16, 18]
l2 = [3, 6, 9, 12, 15, 18, 21]
c = []
for i in l1:
    if i in l2:
        c.append(i)
print("Common elements are:", c)

print("=======================================================")

print("task 10: 2nd smallest element in lists")
num = [2, 6, 4, 8, 10, 12]
num.sort()
print("Second smallest number is: ", num[1])

print("=======================================================")

print("task 11: longest substring without repeating characters")
s = input("Enter string: ")
max_len = 0
ls = ""
for i in range(len(s)):
    temp = ""
    for j in range(i, len(s)):
        if s[j] not in temp:
            temp += s[j]
        else:
            break
    if len(temp) > max_len:
        max_len = len(temp)
        ls = temp
print("Longest substring length:", max_len)
print("Longest substring: ", ls)

print("=======================================================")

print("task 12: first non repeating character")
s = input("Enter string: ")
l = list(s)
for i in range(len(l)-1):
    if l[i] == l[i+1] or l[i-1] == l[i]:
        pass
    else:
        print("first non repeating character is: ", l[i])
        break

