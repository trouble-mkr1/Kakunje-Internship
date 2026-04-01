import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
# '''
# 1. Daily Calorie Tracker 
# Tasks 
# • Enter food item & calories 
# • Store in Pandas 
# • Calculate total daily calories (NumPy) 
# • Show pie chart of calorie intake 
# '''
# print("\nTask 1 output:\n")
# data = {
#     "Food": [],
#     "Calorie": []
#     }
# n = int(input("Enter number of food products: "))
# for i in range(n):
#     food = input("Enter food name: ")
#     cal = int(input("Enter calorie: "))
#     data["Food"].append(food)
#     data["Calorie"].append(cal)
# df = pd.DataFrame(data)
# print()
# total = np.sum(df["Calorie"])
# print("Total Calories:", total)
# plt.pie(df["Calorie"], labels=df["Food"])
# plt.show()

# print("==========================================================")
# ###################################################################
# ###################################################################

# '''
# 2. Inventory Stock Analyzer 
# Tasks 
# • Enter product name & quantity 
# • Store data (Pandas) 
# • Calculate total stock (NumPy) 
# • Display bar graph of stock levels 
# '''
# print("\nTask 2 output:\n")
# data = {
#     "Product": [],
#     "Quantity": []
#     }

# n = int(input("Enter number of products: "))
# for i in range(n):
#     product = input("Enter product name: ")
#     qty = int(input("Enter quantity: "))
#     data["Product"].append(product)
#     data["Quantity"].append(qty)
# df = pd.DataFrame(data)
# print()
# total = np.sum(df["Quantity"])
# print("Total Stock:", total)
# plt.bar(df["Product"], df["Quantity"])
# plt.title("Inventory Stock Analyzer")
# plt.xlabel("Product")
# plt.ylabel("Quantity")
# plt.show()

# print("==========================================================")
# ###################################################################
# ###################################################################

# '''
# 3. Game Score Tracker 
# Tasks 
# • Enter player name & score 
# • Store in Pandas 
# • Calculate highest score (NumPy) 
# • Show score comparison graph
# '''
# print("\nTask 3 output:\n")
# data = {
#     "Player": [],
#     "Score": []
#     }
# n = int(input("Enter number of players: "))
# for i in range(n):
#     player = input("Enter player name: ")
#     score = int(input("Enter score: "))
#     data["Player"].append(player)
#     data["Score"].append(score)
# df = pd.DataFrame(data)
# print()
# highest = np.max(df["Score"])
# print("Highest Score:", highest)
# plt.bar(df["Player"], df["Score"])
# plt.title("Game Score Tracker")
# plt.xlabel("Player")
# plt.ylabel("Score")
# plt.show()

# print("==========================================================")
# ###################################################################
# ###################################################################

# '''
# 4. Traffic Count Analyzer 
# Tasks 
# • Enter vehicle counts per hour 
# • Store data (Pandas) 
# • Calculate peak time (NumPy) 
# • Display traffic graph 
# '''
# print("\nTask 4 output:\n")
# hours = [1, 2, 3, 4, 5]
# traffic = [50, 80, 120, 90, 60]
# df = pd.DataFrame({"Hour": hours, "Traffic": traffic})
# peak = df.iloc[np.argmax(traffic)]
# print("Peak Hour:", peak["Hour"])
# plt.plot(df["Hour"], df["Traffic"])
# plt.show()

# print("==========================================================")
# ###################################################################
# ###################################################################

# '''
# Find: 
# • Accuracy 
# • Precision 
# • Recall 
# • F1-score 
# For the following confusion matrix

#                     Predicted Positive   Predicted Negative 
# Actual Positive             50                   10 
# Actual Negative             5                    35

# TP = 50, FN = 10, FP = 5, TN = 35
# Accuracy = (50 + 35) / (50 + 35 + 10 + 5) = 0.85 
# Precision = 50 / (50 + 5) = 0.90 
# Recall = 50 / (50 + 10) = 0.83 
# F1 Score = (2 * 0.90 * 0.83) / (0.90 + 0.83) = 0.86 

# ==================================================== 

#     Pred A  Pred B  Pred C 
# A      40      5       5 
# B      10      30      10 
# C      5       5       40 

# Accuracy = (40 + 30 + 40) / 150 = 0.76 
# Precision: 
# A = 40 / (40 + 10 + 5) = 0.72 
# B = 30 / (30 + 5 + 5) = 0.75 
# C = 40 / (40 + 5 + 10) = 0.72 
# Recall: 
# A = 40 / (40 + 5 + 5) = 0.8 
# B = 30 / (30 + 10 + 10) = 0.6 
# C = 40 / (40 + 5 + 5) = 0.8 
# F1 Score: 
# A = (2 * 0.72 * 0.8) / (0.72 + 0.8) = 0.75 
# B = (2 * 0.75 * 0.6) / (0.75 + 0.6) = 0.66 
# C = (2 * 0.72 * 0.8) / (0.72 + 0.8) = 0.75

# ====================================================

#                     Pred Positive   Pred Negative 
# Actual Positive         20              80 
# Actual Negative         10              890

# TP = 20, FN = 80, FP = 10, TN = 890 
# Accuracy = (20 + 890) / (20 + 80 + 10 + 890) = 0.91 
# Precision = 20 / (20 + 10) = 0.66 
# Recall = 20 / (80 + 20) = 0.2 
# F1 Score = (2 * 0.66 * 0.2) / (0.66 + 0.2) = 0.30

# ====================================================

#         Pred Yes    Pred No 
# Yes         45          5 
# No          15          35 

# TP = 45, FN = 5, FP = 15, TN = 35 
# Accuracy = (45 + 35) / (45 + 5 + 15 + 35) = 0.8 
# Precision = 45 / (45 + 15) = 0.75 
# Recall = 45 / (45 + 5) = 0.9 
# F1 Score = (2 * 0.75 * 0.9) / (0.75 + 0.9) = 0.81 

# ====================================================
# '''

# print("==========================================================")
# ###################################################################
# ###################################################################

# '''
# NumPy - Task  
# 1. Create a NumPy array of numbers from 1 to 10 and display it
# 2. Find the mean, median, and standard deviation of a NumPy array. 
# 3. Generate 10 random numbers between 0 and 1 using NumPy. 
# 4. Reshape a 1D array into a 2D array. 
# 5. Find the maximum and minimum values in an array. 
# 6. Create an array of zeros and ones using NumPy.
# '''
# print("\nNumpy Tasks: \n")
# # 1
# arr = np.arange(1, 11)
# print(arr)
# print()
# # 2
# print("Mean:", np.mean(arr))
# print("Median:", np.median(arr))
# print("Std Dev:", np.std(arr))
# print()
# # 3
# rand = np.random.rand(10)
# print(rand)
# print()
# # 4
# d2 = arr.reshape(2,5)
# print(d2)
# print()
# # 5
# print("Max:", np.max(arr))
# print("Min:", np.min(arr))
# print()
# # 6
# print(np.zeros((3,3)))
# print(np.ones((3,3)))
# print()

# print("==========================================================")
# ###################################################################
# ###################################################################

# '''
# Pandas - Task Questions 
# 1. Create a Pandas DataFrame with student names and marks. 
# 2. Add a new column to the DataFrame. 
# 3. Sort the DataFrame based on marks. 
# 4. Read a CSV file and display the first 25 rows. 
# 5. Remove missing values from a dataset. 
# 6. Replace the value using median 
# '''
# print("\nPandas Tasks: \n")
# # 1
# data = {
#     "Name": ["Abdul", "Ash", "Random"],
#     "Marks": [90, 100, 50]
# }
# df = pd.DataFrame(data)
# print(df)
# print()
# # 2
# df["Grade"] = ["A","A","D"]
# print(df)
# print()
# # 3
# print(df.sort_values("Marks"))
# print()
# # 4
# df = pd.read_csv("data.csv")
# print(df.head(25))
# print()
# # 5
# df = df.dropna()
# print(df)
# print()
# # 6
# df.fillna(df.median(), inplace=True)
# print(df)
# print()

# print("==========================================================")
# ###################################################################
# ###################################################################

# '''
# Matplotlib - Task Questions 
# 1. Create a line graph showing monthly sales. 
# 2. Plot a bar chart for student marks. 
# 3. Create a scatter plot for height vs weight. 
# 4. Draw a histogram for age distribution. 
# 5. Add title, labels, and legend to a graph. 
# 6. Plot multiple lines on the same graph. 
# 7. Customize color, marker, and grid in a plot.
# '''
# print("\nMatplotlib Tasks: \n")
# # 1
# m = ["Jan", "Feb", "Mar", "Apr"]
# s = [12000, 15000, 20520, 9000]
# plt.plot(m, s)
# plt.show()
# # 2
# plt.bar(data["Name"], data["Marks"])
# plt.show()
# # 3
# h = [150, 155, 165, 130]
# w = [80, 85, 65, 60]
# plt.scatter(h, w)
# plt.show()
# # 4
# age = [18, 25, 20, 34, 15, 46, 26]
# plt.hist(age)
# plt.show()
# # 5, 6 and 7
# x = [1, 2, 3, 4]
# y1 = [10, 20, 30, 40]
# y2 = [90, 80, 70, 60]
# plt.plot(x, y1, label="Line 1", marker='o')
# plt.plot(x, y2, label="Line 2", marker='x')
# plt.title("matplotlib task 5, 6 and 7")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.legend()
# plt.grid()
# plt.show()

# print("==========================================================")
# ###################################################################
# ###################################################################

# '''
# Tkinter - Task Questions 
# 1. Create a basic window using Tkinter. 
# 2. Add a label and button to the window. 
# 3. Create a simple calculator using Tkinter(ADD, SUB, MUL, DIV) 
# 4. Create a login form with username and password fields. 
# 5. Display a message when a button is clicked. 
# 6. Create a text box to accept user input. 
# 7. Build a simple notepad application. 
# 8. Add a menu bar to a Tkinter window. 
# '''
# print("\nTkinter Tasks: \n")
# # 1
# root = tk.Tk()
# root.geometry("100x100")
# root.title("Basic Window")
# root.mainloop()
# # 2
# root = tk.Tk()
# root.geometry("100x100")
# l = tk.Label(root, text="Hello")
# l.pack(pady = "5")
# b = tk.Button(root, text="Click")
# b.pack()
# root.mainloop()
# # 3
# def add():
#     a = int(e1.get())
#     b = int(e2.get())
#     r.config(text = f"Result = {a+b}")
# def sub():
#     a = int(e1.get())
#     b = int(e2.get())
#     r.config(text = f"Result = {a-b}")
# def mul():
#     a = int(e1.get())
#     b = int(e2.get())
#     r.config(text = f"Result = {a*b}")
# def div():
#     a = float(e1.get())
#     b = float(e2.get())
#     r.config(text = f"Result = {a/b}")
# root = tk.Tk()
# root.title("calculator")
# root.geometry("300x500")
# root.configure(bg = "lightblue")
# l1 = tk.Label(root, text = "enter first number")
# l1.pack(pady = "10")
# e1 = tk.Entry(root)
# e1.pack(pady = "10")
# l2 = tk.Label(root, text = "enter second number")
# l2.pack(pady = "10")
# e2 = tk.Entry(root)
# e2.pack(pady = "10")
# a = tk.Button(root, text = "ADD", command = add)
# a.pack(pady = "10")
# s = tk.Button(root, text = "SUB", command = sub)
# s.pack(pady = "10")
# m = tk.Button(root, text = "MUL", command = mul)
# m.pack(pady = "10")
# d = tk.Button(root, text = "DIV", command = div)
# d.pack(pady = "10")
# r = tk.Label(root, text = "")
# r.pack(pady = "10")
# root.mainloop()
# # 4
# def login():
#     if user.get() == "admin" and pwd.get() == "123":
#         res.config(text = "Login succesfull")
#     else:
#         res.config(text = "Invalid Credentials")
# root = tk.Tk()
# root.title("Login")
# root.geometry("300x300")
# root.configure(bg = "white")
# u = tk.Label(root, text = "Username")
# u.pack()
# user = tk.Entry(root)
# user.pack(pady = "10")
# p = tk.Label(root, text = "Password")
# p.pack(pady = "10")
# pwd = tk.Entry(root, show = "*")
# pwd.pack(pady = "10")
# l = tk.Button(root, text = "Login", command = login)
# l.pack(pady = "10")
# res = tk.Label(root, text = "", bg = "white")
# res.pack()
# root.mainloop()
# # 5
# from tkinter import messagebox
# def show_msg():
#     messagebox.showinfo('Info', "Tkinter is easy")
# root = tk.Tk()
# root.title("messege box")
# root.geometry("100x100")
# b = tk.Button(root, text = "show message", command = show_msg)
# b.pack()
# root.mainloop()
# # 6
# root = tk.Tk()
# root.geometry("200x200")
# e = tk.Entry(root, bg = "cyan", fg = "purple")
# e.pack()
# root.mainloop()
# # 7
# root = tk.Tk()
# root.title("Notepad")
# root.geometry("400x400")
# text = tk.Text(root)
# text.pack(expand=True, fill='both')
# root.mainloop()
# # 8
# root = tk.Tk()
# root.title("Menu Example")
# root.geometry("300x200")
# menu_bar = tk.Menu(root)
# file_menu = tk.Menu(menu_bar, tearoff=0)
# file_menu.add_command(label="New")
# file_menu.add_command(label="Open")
# file_menu.add_command(label="Save")
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=root.quit)
# menu_bar.add_cascade(label="File", menu=file_menu)
# root.config(menu=menu_bar)
# root.mainloop()

# print("==========================================================")
# ###################################################################
# ###################################################################

# '''
# PyQt - Task Questions 
# 1. Create a basic PyQt application window. 
# 2. Add buttons and labels to the window. 
# 3. Create a login form using PyQt. 
# 4. Handle button click events. 
# 5. Design a GUI using Qt Designer. 
# '''
# print("\nPyQt Tasks: \n")
# # 1, 2, 3 and 4
# def login():
#     user = username.text()
#     pswd = password.text()
#     if user == "admin" and pswd == "123":
#         result.setText("Login successful")
#     else:
#         result.setText("Invalid credentials")
# app = QApplication(sys.argv)
# window = QWidget()
# window.setWindowTitle("Login Form")
# window.resize(300, 300)
# username = QLineEdit(window)
# username.setPlaceholderText("Enter username")
# password = QLineEdit(window)
# password.setPlaceholderText("Enter password")
# button = QPushButton("Login")
# result = QLabel("", window)
# layout = QVBoxLayout()
# layout.addWidget(username)
# layout.addWidget(password)
# layout.addWidget(button)
# layout.addWidget(result)
# window.setLayout(layout)
# button.clicked.connect(login)
# window.show()
# sys.exit(app.exec_())

# print("==========================================================")
# ###################################################################
# ###################################################################

'''
NLTK - Task Questions 
1. Perform word tokenization using NLTK. 
2. Perform sentence tokenization on a paragraph. 
3. Remove stop words from a sentence. 
4. Apply stemming using PorterStemmer. 
5. Perform lemmatization using WordNetLemmatizer. 
6. Perform Part-of-Speech tagging on a sentence.
'''
print("\nNLTK Tasks: \n")
# 1
text = "Online shopping has become very convenient today. Customers expect fast delivery and good product quality."
words = word_tokenize(text)
print("word tokens are: ", words)
print()
# 2
sentence = sent_tokenize(text)
print("sentence tokens are: ", sentence)
print()
# 3
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

# print("==========================================================")
# ###################################################################
# ###################################################################
