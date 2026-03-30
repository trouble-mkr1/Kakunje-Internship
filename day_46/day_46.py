'''
1. Consider a string 
Machine Learning 
Using string methods, get output: 
• MACHINE LEARNING 
• machine learning 
• ['Machi', 'e Lear', 'i', 'g']  
'''
print("\ntask 1 output\n")
t = "Machine Learning"
print(t.upper())
print(t.lower())
print([t[0:5], t[6:12], t[-3], t[-1]])

print("====================================================================")
#############################################################################
#############################################################################

'''
2. Consider a string 
Plants need air, water and sunlight to grow 
Using string slicing, get output 
• air, water and 
• ,ria deen stnalP 
• ndi t duit 
• worg ot thgilnus dna retaw ,ria deen stnalP 
• anaw sgow 
'''
print("\ntask 2 output\n")
s = "Plants need air, water and sunlight to grow"
print(s[12:26])
print(s[15::-1])
print(s[7:35:3])
print(s[::-1])
print(s[2::5])

print("====================================================================")
#############################################################################
#############################################################################

'''
3. Consider a string 
Indentation is very important in Python 
Using string slicing, get output 
• tnatropmi 
• otPn ntom 
• si noitatnednI 
'''
print("\ntask 3 output\n")
s = "Indentation is very important in Python"
print(s[-11:-21:-1])
print(s[-2:-20:-2])
print(s[13::-1])

print("====================================================================")
#############################################################################
#############################################################################

'''
4. Create a list 
[10,20,30,40,50] 
• Add 35 in between 30 and 40 
• Add 60 at last 
'''
print("\ntask 4 output\n")
l = [10, 20, 30, 40, 50]
l.insert(3, 35)
print(l)
l.append(60)
print(l)

print("====================================================================")
#############################################################################
#############################################################################

'''
5.  Create a List
[“Lion”, “Tiger”, “Elephant”, “Leopard”] 
• Add “Cheetah” in between “Lion” and “Tiger” 
• Add “Monkey” at last 
• Add “Giraffe” in the beginning 
'''
print("\ntask 5 output\n")
l = ["Lion", "Tiger", "Elephant", "Leopard"]
l.insert(1, "Cheetah")
print(l)
l.append("Monkey")
print(l)
l.insert(0, "Giraffe")
print(l)

print("====================================================================")
#############################################################################
#############################################################################

'''
6. Create a tuple and print the tuple. Delete any item from the tuple
'''
print("\ntask 6 output\n")
t = (10, 20, 30, 40, 50)
print(t)
l = list(t)
l.pop(3)
t = tuple(l)
print(t)

print("====================================================================")
#############################################################################
#############################################################################

'''
7. consider matrix
    [ 1, 2, 3, 4 ]
A = [ 5, 6, 7, 8 ]
    [ 9, 10, 11, 12 ]
    [ 13, 14, 15, 16 ]
Get output as: 
• [5,6,7,8] 
• [9,10,11,12] [13,14,15,16] 
• [1,5,9,13] 
• [7,8] [11,12] 
• [1,6,11,16] 
• [4,7,10,13]
'''
print("\ntask 7 output\n")
A =  [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]
print(A[1])
print(A[2:])
print([A[i][0] for i in range(len(A))])
print([A[1][2:], A[2][2:]])
print([A[0][0], A[1][1], A[2][2], A[3][3]])
print([A[0][3], A[1][2], A[2][1], A[3][0]])

print("====================================================================")
#############################################################################
#############################################################################

'''
8. consider matrix:
    [ 1, 2, 3, 4 ]
S = [ 2, 5, 6, 7 ]
    [ 3, 6, 8, 9 ]
    [ 4, 7, 9, 10 ]
• Add row [6,6,6,6] at last 
• Add row [20,25,30,35] in between [3,6,8,9] and [4,7,9,10]
'''
print("\ntask 8 output\n")
S =  [[1, 2, 3, 4],
      [2, 5, 6, 7],
      [3, 6, 8, 9],
      [4, 7, 9, 10]]
S.append([6, 6, 6, 6])
print(S)
S.insert(3, [20, 25, 30, 35])
print(S)

print("====================================================================")
#############################################################################
#############################################################################

'''
9. Task: Password Strength Checker 
Create a function: 
It should: 
• Use loops to check:  
o At least 1 uppercase  
o At least 1 lowercase  
o At least 1 number  
o At least 1 special character  
• Return:  
o "Weak", "Medium", or "Strong"
'''
print("\ntask 9 output\n")
pswd = input("Enter password: ")
def check(pswd):
    strength = 0
    for char in pswd:
        if char.isupper():
            strength += 1
            break
    for char in pswd:
        if char.islower():
            strength += 1
            break
    for char in pswd:
        if char.isdigit():
            strength += 1
            break
    spc = "!@#$%&*-_<>?"
    for char in pswd:
        if char in spc:
            strength += 1
            break
    if strength <= 2:
        print("Weak")
    elif strength == 3:
        print("Medium")
    else:
        print("Strong")
check(pswd)

print("====================================================================")
#############################################################################
#############################################################################

'''
10. Create classes: 
Features: 
• Add books  
• Issue books  
• Return books  
• Show available books
'''
print("\ntask 10 output\n")
class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"{book} added to library")
    
    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"{book} issued")
        else:
            print(f"{book} not available")
    
    def return_book(self, book):
        self.books.append(book)
        print(f"{book} returned")
    
    def show_available_books(self):
        print("Available books:")
        for book in self.books:
            print(book)
library = Library()
library.add_book("Python book")
library.add_book("JAVA book")
library.add_book("C++ book")
library.show_available_books()
library.issue_book("Python book")
library.show_available_books()
library.return_book("Python book")
library.show_available_books()

print("====================================================================")
#############################################################################
#############################################################################

'''
11. Task: Mini ATM System 
• PIN authentication  
• Deposit / Withdraw  
• Balance check  
• Exit option  
Add: 
• 3 wrong attempts → block account
'''
print("\ntask 11 output\n")
class ATM:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance
        self.attempts = 0
    
    def authenticate(self, entered_pin):
        if entered_pin == self.pin:
            self.attempts = 0
            return True
        else:
            self.attempts += 1
            if self.attempts >= 3:
                print("Account blocked")
                return False
            print("Wrong PIN")
            return False
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
    
    def check_balance(self):
        print(f"Balance: {self.balance}")
atm = ATM("1234", 1000)
while True:
    pin = input("Enter PIN: ")
    if atm.authenticate(pin):
        break
while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        atm.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        atm.withdraw(amount)
    elif choice == "3":
        atm.check_balance()
    elif choice == "4":
        print("exiting")
        break
    else:
        print("Invalid choice.")

print("====================================================================")
#############################################################################
#############################################################################

'''
12. Task: Student Data Analysis 
Use pandas 
Dataset: 
Create a CSV with: 
Name, Marks, Subject 
Tasks: 
• Find average marks  
• Find topper  
• Filter students > 75 
'''
import pandas as pd
print("\ntask 12 output\n")
data = {
    "Name": ["Ash", "Abdul", "Random", "Someone"],
    "Marks": [99, 92, 58, 67],
    "Subject": ["Math", "Science", "English", "History"]
}
df = pd.DataFrame(data)
df.to_csv("students.csv", index = False)
df = pd.read_csv("students.csv")
print("Average marks:", df["Marks"].mean())
print("Topper:", df.loc[df["Marks"].idxmax()]["Name"])
print("Students with marks > 75:")
print(df[df["Marks"] > 75])

print("====================================================================")
#############################################################################
#############################################################################

'''
13. Task: Sales Dashboard 
Use Matplotlib 
Requirements: 
Create:  
• Bar chart (sales per product)  
• Line chart (monthly growth)  
• Pie chart (category share)  
'''
import matplotlib.pyplot as plt
print("\ntask 13 output\n")
products = ["Product A", "Product B", "Product C"]
sales = [150, 200, 100]
plt.bar(products, sales)
plt.title("Sales per Product")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()
months = ["Jan", "Feb", "Mar", "Apr", "May"]
growth = [11, 10, 12, 17, 20]
plt.plot(months, growth, marker = "o")
plt.title("Monthly Growth")
plt.xlabel("Months")
plt.ylabel("Growth")
plt.show()
categories = ["Category A", "Category B", "Category C"]
shares = [40, 35, 25]
plt.pie(shares, labels = categories)
plt.title("Category Share")
plt.show()

print("====================================================================")
#############################################################################
#############################################################################

'''
14. Task: GUI Prediction App 
Use: 
• Tkinter  
• scikit-learn  
Requirements: 
• Train model (Any dataset can be used)  
• Save model using joblib  
• Create GUI:  
o Input fields  
o Predict button  
o Show result  
'''
print("\ntask 14 output\n")
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
import joblib
df = pd.read_csv("Iris.csv")
x = df.drop(columns = ["Id", "Species"])
y = df["Species"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)
model = KNeighborsClassifier()
print("Model Accuracy")
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
acc = accuracy_score(y_test, y_pred)
print(f"Model trained successfully. Model accuracy: {acc * 100}%")
joblib.dump(model, "model.pkl")
print("Model saved as \"model.pkl\"")


import tkinter as tk
try:
    model = joblib.load("model.pkl")
except:
    print("Model has not been trained")
df = pd.read_csv("Iris.csv")
def predict():
    values = [float(e1.get()),
              float(e2.get()),
              float(e3.get()),
              float(e4.get())]
    prediction = model.predict([values])[0]
    result.config(text = f"Pridection: {prediction}")
root = tk.Tk()
root.title("Iirs prediction app")
root.geometry("350x400")
tk.Label(root, text = "Enter Iris Features",
         font = ("Arial", 14)).pack(pady = 10)
labels = ["Sepal Length", "Sepal Width",
          "petal Length", "petal Width"]
entries = []
for label in labels:
    tk.Label(root, text = label).pack()
    entry = tk.Entry(root)
    entry.pack()
    entries.append(entry)
e1, e2, e3, e4 = entries
tk.Button(root, text = "Predict", command = predict).pack(pady = 15)
result = tk.Label(root, text = "", font = ("Arial", 12))
result.pack()
root.mainloop()

print("====================================================================")
#############################################################################
#############################################################################

'''
15. Task: Online Shopping Cart System (OOPs) 
Features: 
• Add product  
• Remove product  
• Calculate total bill  
• Apply discount  
• Display cart items  
'''
print("\ntask 15 output\n")
class ShoppingCart:
    def __init__(self):
        self.cart = []
    
    def add_product(self, product, price):
        self.cart.append((product, price))
        print(f"{product} added to cart")
    
    def remove_product(self, product):
        for item in self.cart:
            if item[0] == product:
                self.cart.remove(item)
                print(f"{product} removed from cart")
                return
        print(f"{product} not found in cart")
    
    def calculate_total(self):
        return sum(price for _, price in self.cart)
    
    def apply_discount(self, discount):
        total = self.calculate_total()
        discounted_total = total * (1 - discount / 100)
        print(f"Total after {discount}% discount: {discounted_total}")
    
    def display_cart_items(self):
        print("Cart items:")
        for product, price in self.cart:
            print(f"{product}: {price}")
cart = ShoppingCart()
cart.add_product("Laptop", 70000)
cart.add_product("Phone", 24000)
cart.display_cart_items()
print(f"Total bill: {cart.calculate_total()}")
cart.apply_discount(10)
cart.remove_product("Phone")
cart.display_cart_items()

print("====================================================================")
#############################################################################
#############################################################################

'''
16. Task: Student Result Management System 
Features: 
Store:  
• name  
• marks (multiple subjects)  
Methods:  
• calculate total  
• calculate average  
• assign grade
'''
print("\ntask 16 output\n")
class Student:
    def __init__(self, name):
        self.name = name
        self.marks = {}
    
    def add_marks(self, subject, marks):
        self.marks[subject] = marks
    
    def calculate_total(self):
        return sum(self.marks.values())
    
    def calculate_average(self):
        return self.calculate_total() / len(self.marks)
    
    def assign_grade(self):
        average = self.calculate_average()
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
student = Student("Ash")
student.add_marks("Math", 95)
student.add_marks("Science", 88)
student.add_marks("English", 76)
print(f"Total marks for {student.name}: {student.calculate_total()}")
print(f"Average marks for {student.name}: {student.calculate_average()}")
print(f"Grade for {student.name}: {student.assign_grade()}")
