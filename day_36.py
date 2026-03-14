# Task 1

import tkinter as tk

def convert():
    c = int(e.get())
    result.config(text = f"Fahreneit value is {(c * 1.8) + 32} F")

root = tk.Tk()
root.title("Temperature converter")
root.geometry("300x300")

tk.Label(root, text = "Enter the Celsius value").pack(pady = "10")
e = tk.Entry(root)
e.pack(pady = "10")
b = tk.Button(root, text = "Convert to fahrenheit", command = convert)
b.pack(pady = "10")
result = tk.Label(root, text = "")
result.pack()
root.mainloop()

print("=====================================================")
##############################################################
##############################################################

# Task 2

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rand = []

def gen():
    for _ in range(10):
        rand.append(np.random.randint(10))
    result.config(text = f"Generated random numbers: \n{rand}\n"\
                  f"Mean = {np.mean(rand)}\n"\
                  f"Median = {np.median(rand)}\n"\
                  f"Standard Deviation = {np.std(rand)}\n")
def his():
    df = pd.DataFrame(rand)
    plt.hist(df)
    plt.show()

root = tk.Tk()
root.title("Task 2")
root.geometry("300x300")

tk.Button(root, text = "click to generate random 10 numbers", command = gen).pack(pady = "10")
result = tk.Label(root, text = "")
result.pack(pady = "10")
tk.Button(root, text = "click to generate histogram", command = his).pack(pady = "10")
root.mainloop()

print("=====================================================")
##############################################################
##############################################################

# task 3

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Book Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)

b1 = Book("something", "Sam", 300)
b1.display()
print()
b2 = Book("random", "Mark", 450)
b2.display()

print("=====================================================")
##############################################################
##############################################################

# task 4

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_cart(self):
        print("\nProducts in Cart:")
        for p in self.products:
            print(p.name)

    def total_price(self):
        total = 0
        for i in self.products:
            total += i.price
        return total

p1 = Product("Laptop", 50000)
p2 = Product("Mouse", 500)
cart = Cart()
cart.add_product(p1)
cart.add_product(p2)
cart.display_cart()
print()
print("Total price:", cart.total_price())

print("=====================================================")
##############################################################
##############################################################

# task 5

class ATM:
    def __init__(self):
        self.balance = 1000

    def check_balance(self):
        print("Current Balance:", self.balance)

    def deposit(self):
        amount = int(input("Enter amount to deposit: "))
        self.balance += amount
        print("Amount deposited successfully")

    def withdraw(self):
        amount = int(input("Enter amount to withdraw: "))
        self.balance -= amount
        print("Amount withdrawed successfully")

atm = ATM()
while True:
    print("\n\tATM menu")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        atm.check_balance()
    elif ch == 2:
        atm.deposit()
    elif ch == 3:
        atm.withdraw()
    elif ch == 4:
        print("Exiting")
        break
    else:
        print("Invalid choice")

print("=====================================================")
##############################################################
##############################################################

# task 6

class Student:
    def __init__(self, name):
        self.name = name

class Teacher:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []
        self.teacher = None

    def add_student(self, student):
        self.students.append(student)

    def assign_teacher(self, teacher):
        self.teacher = teacher

    def display(self):
        print("Course:", self.course_name)
        print("Teacher:", self.teacher.name)
        print("Students:")
        for s in self.students:
            print(s.name)

s1 = Student("Abdul")
s2 = Student("Ash")
t1 = Teacher("Miss Pragathi")
course = Course("Python")
course.add_student(s1)
course.add_student(s2)
course.assign_teacher(t1)
course.display()

print("=====================================================")
##############################################################
##############################################################

# task 7

n = []
for num in range(2, 101):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        n.append(num)
print("Prime numbers are:", n)

print("=====================================================")
##############################################################
##############################################################

# task 8

x = "ABCDEFGHIJK"

print(x[2:10:2])
print(x[:-9:-1])
print(x[:-11:-1])
print(x[:-8:-2])
print(x[::4])
print()

x = "Python String Slicing Example"

print(x[:14])
print(x[14:])
print(x[::-3])
print(x[::4])
print(x[:-8:-1])
print(x[12::-4])

print("=====================================================")
##############################################################
##############################################################

# task 9

'''
["Cat", "Dog", "Lion", "Tiger", "Rabbit", "Monkey"]
1) ["lion"]
2) ["Monkey", "Rabbit"]
3) ["Tiger", "Lion", "Dog"]
4) ["Cat", "Tiger"]
5) ["Tiger", "Cat"]
6) ["Monkey", "Lion"]
7) ["Rabbit", "Lion", "Cat"]
8) ["Monkey", "Rabbit", "Tiger", "Lion", "Dog", "Cat"]
'''

l = ["Cat", "Dog", "Lion", "Tiger", "Rabbit", "Monkey"]

print(l[2:3])
print(l[:-3:-1])
print(l[3:0:-1])
print(l[::3])
print(l[-3::-3])
print(l[::-3])
print(l[-2::-2])
print(l[::-1])
print()

'''
["apple", "banana", "cherry"]
1. ["apple", "banana", "cherry", "orange"]
2. ["apple", "mango", "banana", "cherry", "orange"]
3. ["apple", "mango", "banana", "cherry", "orange", "kiwi", "grape"]
'''

l = ["apple", "banana", "cherry"]
l.append("orange")
print(l)
l.insert(1, "mango")
print(l)
l.append("kiwi")
l.append("grape")
print(l)
print()

'''
[10,20,30,40,50]
1. [10,20,300,40,50]
2. [10,200,3000,400,50]
'''

l = [10, 20, 30, 40, 50]

l[2] = 300
print(l)
l[1] = 200
l[2] = 3000
l[-2] = 400
print(l)
print()

'''
[1,2,3]
1. [1,100,2,3]
2. [1,100,2,999]
'''

l = [1, 2, 3]

l.insert(1, 100)
print(l)
l[-1] = 999
print(l)
print()

'''
[10,20,30,40,50]
1. [10,20,30,40,50,60]
2. [5,10,20,30,40,50,60]
3. [5,10,20,30,40,50,60,70,80,90]
'''

l = [10, 20, 30, 40, 50]

l.append(60)
print(l)
l.insert(0, 5)
print(l)
l.append(70)
l.append(80)
l.append(90)
print(l)
print()

'''
[42,3.14,"Hello",True]
1. [2.718,3.14,"Hello",True]
2. [2.718,3.14,"Hello",True,1000]
3. [2.718,False,3.14,"Hello",True,1000]
4. [5,3.14,"Hello",True,1000]
'''

l = [42, 3.14, "Hello", True]

l[0] = 2.718
print(l)
l.append(1000)
print(l)
l.insert(1, False)
print(l)
l[0] = 5
l.pop(1)
print(l)
print()

'''
"Hello World, Welcome to Python!"
1. Convert all characters into uppercase
2. Convert all characters into lowercase
3. Split the string based on space
4. Split the string based on character o
5. Replace character W with character X
'''

s = "Hello World, Welcome to Python!"

print(s.upper())
print(s.lower())
print(s.split(" "))
print(s.split("o"))
print(s.replace("W", "X"))