'''
Task 1: Electricity Bill Calculator
Create a function calculate_bill(units):
•	If units ≤ 100 → ₹1/unit
•	101-200 → ₹2/unit
•	200 → ₹3/unit
Return the total bill amount
'''
print("task 1: electricity bill calculator\n")

def calculate_bill(unit):
    if(unit <= 100):
        print(f"Electricity Bill = {unit * 1} rs")
    elif(unit <= 200):
        print(f"Electricity Bill = {unit * 2} rs")
    else:
        print(f"Electricity Bill = {unit * 3} rs")

unit = int(input("enter the electricity unit consumed: "))
calculate_bill(unit)

print("======================================================================")
###############################################################################
###############################################################################
'''
Task 2: Password Strength Checker
Write a function check_password(password) that checks:
•	Length ≥ 8
•	Contains at least one digit
•	Contains at least one special character
Return "Strong" or "Weak".
'''
print("task 2: password strength checker\n")

def check_strength(password):
    digit = "0123456789"
    spc_char = "!@#$%^&*()_+=/\\"
    a = False
    b = False
    if(len(password)<8):
        print("length must be atleast 8 characters long!")
        return
    for char in password:
        if char in digit:
            a = True
        if char in spc_char:
            b = True
    if a and b:
        print("strong password")
    else:
        print("weak password")

password = input("enter the password: ")
check_strength(password)

print("======================================================================")
###############################################################################
###############################################################################
'''
Task 3: Reverse a Number Using Loop
•	Input a number and reverse it using a while loop.
'''
print("task 3: reverse of a string")

num = int(input("enter a number: "))
rev = 0
while(num>0):
    digit = num % 10
    rev = rev*10 + digit
    num = num // 10
print(f"reverse number  = {rev}")

print("======================================================================")
###############################################################################
###############################################################################
'''
Task 4: Count Vowels in a String
•	Using a for loop, count how many vowels are present in a given string.
'''
print("task 4: count vowels")

word = input("enter a word: ")
v = "aeiouAEIOU"
count = 0
for char in word:
    if char in v:
        count+=1
print(f"number of vowels in {word} is: {count}")

print("======================================================================")
###############################################################################
###############################################################################
'''
Task 5: ATM Withdrawal System
Input:
•	Account balance
•	Withdrawal amount
Conditions:
•	Amount should be a multiple of 100
•	Amount ≤ balance
Display success or error message.
'''
print("task 5: ATM withdraw machine")

balance = int(input("enter the account balance: "))
amount = int(input("enter the amount to withdraw: "))
x = False
if amount>balance:
    print(f"cannot withdraw more than {balance}")
    print(f"available balance: {balance}")
elif amount%100 != 0:
    print(f"withdraw amount must be in multiple of 100")
    print(f"available balance: {balance}")
else:
    balance = balance - amount
    print(f"available balance: {balance}")
    x = True
if x:
    print("withdraw successfull!!")
else:
    print("ERROR!! unsuccessfull withdraw")

print("======================================================================")
###############################################################################
###############################################################################
'''
Task 6: Student Grade with Remarks
Based on marks:
•	≥90 → A (Excellent)
•	75-89 → B (Very Good)
•	60-74 → C (Good)
•	<60 → Fail
'''
print("task 6: student grading on marks\n")

marks = int(input("enter marks: "))
if marks>=90:
    print("Grade A, Excellent")
elif marks>=75:
    print("Grade B, Very Good")
elif marks>=60:
    print("Grade C, Good")
else:
    print("Fail")

print("======================================================================")
###############################################################################
###############################################################################
'''
Task 7: Mobile Phone Class
Create a Mobile class with:
•	brand
•	model
•	price
Methods:
•	display_details()
'''
print("task 7: mobile phone class\n")

class mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_details(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}")

mob1 = mobile("Samsung", "S22 Ultra", 120000)
mob2 = mobile("Nothing", "3A Pro", 60000)
mob1.display_details()
mob2.display_details()

print("======================================================================")
###############################################################################
###############################################################################
'''
Task 8: Inheritance - Employee Salary
•	Base class: Employee (name, id)
•	Derived class: PermanentEmployee (basic_salary)
•	Method to calculate salary
'''
print("task 8: Inheritance class\n")

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class salary(Employee):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, ID: {self.id}, Salary: {self.salary}")

a = salary("Abdul",111, 1200000)
a.display()

print("======================================================================")
###############################################################################
###############################################################################
'''
Task 9: Palindrome Checker (Number & String)
Use:
•	Function
•	Loop
•	Conditional
Check if input is palindrome.
'''
print("task 9: check for palindrome\n")
def check_pal_num(num):
    n = num
    rev = 0
    while(num>0):
        digit = num % 10
        rev = rev*10 + digit
        num = num // 10
    if n == rev:
        print(f"number {n} is a palindrome. reverse of {n} is {rev}")
    else:
        print(f"number {n} is not a palindrome. reverse of {n} is {rev}")
def check_pal_word(word):
    rev_word = word[::-1]
    if rev_word == word:
        print(f"word {word} is a palindrome. reverse of {word} is {rev_word}")
    else:
        print(f"word {word} is not a palindrome. reverse of {word} is {rev_word}")
print("enter 1 to check palindrome for number")
print("enter 2 to check palindrome for word")
x = int(input("\nEnter your choice(1 or 2)"))
if x==1:
    num = int(input("enter number to check palindrome: "))
    check_pal_num(num)
elif x==2:
    word = input("enter word to check palindrome: ")
    check_pal_word(word)
else:
    print("the only options are either 1 or 2")







    

