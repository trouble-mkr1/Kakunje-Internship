# NUMPY TASKS

import numpy as np
# 1
arr = np.arange(1, 11)
print(arr)
print()

# 2
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Std Dev:", np.std(arr))
print()

# 3
rand = np.random.rand(10)
print(rand)
print()

# 4
d2 = arr.reshape(2,5)
print(d2)
print()

# 5
print("Max:", np.max(arr))
print("Min:", np.min(arr))
print()

# 6
print(np.zeros((3,3)))
print(np.ones((3,3)))
print()

print("=====================================================")
##############################################################
##############################################################

# PANDAS TASKS

import pandas as pd
# 1
data = {
    "Name": ["Abdul", "Ash", "Random"],
    "Marks": [90, 100, 50]
}
df = pd.DataFrame(data)
print(df)
print()

# 2
df["Grade"] = ["A","A","D"]
print(df)
print()

# 3
print(df.sort_values("Marks"))
print()

# 4
df = pd.read_csv("data.csv")
print(df.head(25))
print()

# 5
df = df.dropna()
print(df)
print()

# 6
df.fillna(df.median(), inplace=True)
print(df)
print()

print("=====================================================")
##############################################################
##############################################################

# MATPLOTLIB TASKS

import matplotlib.pyplot as plt
# 1
m = ["Jan", "Feb", "Mar", "Apr"]
s = [12000, 15000, 20520, 9000]
plt.plot(m, s)
plt.show()

# 2
plt.bar(data["Name"], data["Marks"])
plt.show()

# 3
h = [150, 155, 165, 130]
w = [80, 85, 65, 60]
plt.scatter(h, w)
plt.show()

# 4
age = [18, 25, 20, 34, 15, 46, 26]
plt.hist(age)
plt.show()

print("=====================================================")
##############################################################
##############################################################

# TKINTER TASKS

import tkinter as tk
# 1
root = tk.Tk()
root.geometry("100x100")
root.title("Basic Window")
root.mainloop()

# 2
root = tk.Tk()
root.geometry("100x100")
l = tk.Label(root, text="Hello")
l.pack(pady = "5")
b = tk.Button(root, text="Click")
b.pack()
root.mainloop()

# 3
def add():
    a = int(e1.get())
    b = int(e2.get())
    r.config(text = f"Result = {a+b}")
def sub():
    a = int(e1.get())
    b = int(e2.get())
    r.config(text = f"Result = {a-b}")
def mul():
    a = int(e1.get())
    b = int(e2.get())
    r.config(text = f"Result = {a*b}")
def div():
    a = float(e1.get())
    b = float(e2.get())
    r.config(text = f"Result = {a/b}")
root = tk.Tk()
root.title("calculator")
root.geometry("300x500")
root.configure(bg = "lightblue")
l1 = tk.Label(root, text = "enter first number")
l1.pack(pady = "10")
e1 = tk.Entry(root)
e1.pack(pady = "10")
l2 = tk.Label(root, text = "enter second number")
l2.pack(pady = "10")
e2 = tk.Entry(root)
e2.pack(pady = "10")
a = tk.Button(root, text = "ADD", command = add)
a.pack(pady = "10")
s = tk.Button(root, text = "SUB", command = sub)
s.pack(pady = "10")
m = tk.Button(root, text = "MUL", command = mul)
m.pack(pady = "10")
d = tk.Button(root, text = "DIV", command = div)
d.pack(pady = "10")
r = tk.Label(root, text = "")
r.pack(pady = "10")
root.mainloop()

# 4
def login():
    if user.get() == "admin" and pwd.get() == "123":
        res.config(text = "Login succesfull")
    else:
        res.config(text = "Invalid Credentials")

root = tk.Tk()
root.title("Login")
root.geometry("300x300")
root.configure(bg = "white")
u = tk.Label(root, text = "Username")
u.pack()
user = tk.Entry(root)
user.pack(pady = "10")
p = tk.Label(root, text = "Password")
p.pack(pady = "10")
pwd = tk.Entry(root, show = "*")
pwd.pack(pady = "10")
l = tk.Button(root, text = "Login", command = login)
l.pack(pady = "10")
res = tk.Label(root, text = "", bg = "white")
res.pack()
root.mainloop()

# 5
from tkinter import messagebox
def show_msg():
    messagebox.showinfo('Info', "Tkinter is easy")
root = tk.Tk()
root.title("messege box")
root.geometry("100x100")
b = tk.Button(root, text = "show message", command = show_msg)
b.pack()
root.mainloop()

# 6
root = tk.Tk()
root.geometry("200x200")
e = tk.Entry(root, bg = "cyan", fg = "purple")
e.pack()
root.mainloop()

print("=====================================================")
##############################################################
##############################################################

# PYQT5 TASK

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

print("=====================================================")
##############################################################
##############################################################

# NLTK TASKS

import nltk
from nltk.tokenize import word_tokenize
# 1
text = "Online shopping has become very convenient today. Customers expect fast delivery and good product quality."
words = word_tokenize(text)
print("word tokens are: ", words)
print()

# 2
from nltk.tokenize import sent_tokenize
sentence = sent_tokenize(text)
print("sentence tokens are: ", sentence)
print()

# 3
from nltk.corpus import stopwords
words = word_tokenize(sentence[0])
stop_words = set(stopwords.words("english"))
filtered_words = []
for w in words:
    if w.lower() not in stop_words:
        filtered_words.append(w)
print("Original words: ")
print(words)
print()
print("Filtered words(Stopwords Removed): ")
print(filtered_words)

# 4
from nltk.stem import PorterStemmer
ps = PorterStemmer()
words = ["delivery", "delivering", "delivered", "customers", "shopping", "quality"]
w = []
for i in words:
    w.append(ps.stem(i))
print("Original words: ")
print(words)
print()
print("Stemmed words: ")
print(w)
print()

# 5
from nltk.stem import WordNetLemmatizer
lemm = WordNetLemmatizer()
words = ["running", "better", "customers", "products"]
l = []
for w in words:
    l.append(lemm.lemmatize(w))
print()
print("Original words:")
print(words)
print("Lemmatized words:")
print(l)

# 6
pos = nltk.pos_tag(word_tokenize(sentence[0]))

print()
print("POS Tags:")
print(pos)


