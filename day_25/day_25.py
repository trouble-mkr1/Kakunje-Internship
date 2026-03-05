'''
 TASK 1 - User Registration Module (EdTech Platform)
You are building a student registration system for an online learning platform.
Before storing data in a database, you must validate and format user input properly.
(Use Numeric types (int, float),Type conversion, Strings ,Indexing & slicing,  
Stringmethods, String formatting, Escape characters)
Task Requirements
1.	Take user input:
    o	Full Name
    o	Age
    o	Course Fee
    o	Email
2.	Perform:
    o	Extract first name using slicing
    o	Print initials using indexing
    o	Convert age to integer
    o	Format output using f-string
    o	Convert email to lowercase
    o	Display a welcome message using escape characters (\n, \t)
'''
print("TASK 1 - User Registration Module (EdTech Platform)")
print("\tWelcome to AIML Academy!\n")
full_name = input("Enter Full Name: ")
age = input("Enter Age: ")
fee = input("Enter Course Fee: ")
email = input("Enter Email: ")
age = int(age)
fee = float(fee)
print("first name is: ", full_name[:full_name.index(" ")])
names = full_name.split()
initials = names[0][0] + "." + names[1][0]
email = email.lower()
print("\nStudent Registration Details")
print(f"Student Name: {full_name}")
print(f"Initials: {initials}")
print(f"Age: {age}")
print(f"Course Fee: ₹{fee:.2f}")
print(f"Email: {email}")

print("======================================================================")
###############################################################################
###############################################################################
'''
TASK 2 - Sales Data Tracker (Retail Store)
You are working as a Python intern in a retail company.Your task is
 to track daily product sales.
(Use Lists,Append, insert, remove,Sorting,Reverse,Membership operator,
Arithmetic operators,For loop,If-else
 Task Requirements
1.	Ask user to enter 5 daily sales amounts.
2.	Store them in a list.
3.	Calculate:
    o	Total revenue
    o	Average revenue
4.	Sort sales in ascending & descending order.
5.	Remove the lowest sale value.
6.	Check if any sale is below ₹1000 → print "Low Sales Alert".
'''
print("TASK 2 - Sales Data Tracker (Retail Store)")
sales = []
for i in range(1, 6):
    amount = int(input(f"Enter sale amount {i}: "))
    sales.append(amount)
print("\nDaily Sales:", sales)
total= sum(sales)
average = total / len(sales)
print("Total Revenue:", total)
print("Average Revenue:", average)
a = sorted(sales)
print("Ascending Order:", a)
d = sorted(sales, reverse=True)
print("Descending Order:", d)
lowest = min(sales)
sales.remove(lowest)
print("Lowest sale removed:", lowest)
print("Updated Sales List:", sales)
for sale in sales:
    if sale < 1000:
        print("Low Sales Alert Triggered!")
        break

print("======================================================================")
###############################################################################
###############################################################################
'''
TASK 3 - Employee Skill Management System (HR Tech)
You are developing an internal HR tool to track employee 
skills and departments.
(use  Dictionary,Nested dictionary,Tuple,Set,Union, intersection,
keys(), values(), items())
 Task Requirements
1.	Store employee details in dictionary:
    o	ID
    o	Name
    o	Department
    o	Skills (Set)
2.	Add new skill.
3.	Compare skills of two employees using:
    o	Union
    o	Intersection
4.	Store salary grade as tuple.
5.	Unpack tuple.
6.	Print dictionary using items().
'''
print("TASK 3 - Employee Skill Management System (HR Tech)\n")
t = ("Grade A", 50000, 70000)
grade, min_sal, max_sal = t
emp1 = {
    "ID": 101,
    "Name": "Rahul",
    "Department": "AI",
    "Skills": {"Python", "ML", "SQL", "NLP"}
}
emp2 = {
    "ID": 102,
    "Name": "Anita",
    "Department": "Data",
    "Skills": {"Python", "SQL", "Deep Learning"}
}
emp1["Skills"].add("Deep Learning")
all = emp1["Skills"].union(emp2["Skills"])
common = emp1["Skills"].intersection(emp2["Skills"])
print("All Skills (Union):", all)
print("Common Skills (Intersection):", common)
print("\nSalary Grade:", grade)
print(f"Salary Range: {min_sal} - {max_sal}")
print("\nEmployee 1 Details:")
for key, value in emp1.items():
    print(f"{key} : {value}")

print("======================================================================")
###############################################################################
###############################################################################
'''
 TASK 4 - Hospital Management System (OOP Based)
You are building backend logic for a hospital software.

(use Class & Object,Inheritance,Encapsulation,Polymorphism,
Functions,Exception handling
 Task Requirements
1.	Create base class Person.
2.	Create derived class Doctor and Patient.
3.	Use private variable for medical record.
4.	Override method get_details() (polymorphism).
5.	Raise exception if patient age < 0.
6.	Use try-except block for safe execution.
'''
print("TASK 4 - Hospital Management System (OOP Based)\n")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_details(self):
        return (f"Name: {self.name}, Age: {self.age}")
    
class Doctor(Person):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec
    def get_details(self):
        return f"Doctor Dr. {self.name}, Specialization: {self.spec}"

class Patient(Person):
    def __init__(self, name, age, rec):
        if age < 0:
            raise ValueError("Age cannot be negative!")
        super().__init__(name, age)
        self.rec = rec
    def get_details(self):
        return f"Patient {self.name}, Age: {self.age}"

try:
    doc = Doctor("Mehta", 45, "Cardiology")
    pat = Patient("Ravi", 30, "Heart Patient")
    print(doc.get_details())
    print(pat.get_details())
except ValueError as e:
    print("Error:", e)

print("======================================================================")
###############################################################################
###############################################################################
'''
TASK 5 - Mini Data Analysis Project 
(Use NumPy arrays(1D,2D) ,reshape(), sort(), where(), Pandas, DataFrame,
fillna(), drop_duplicates(), describe())
Task Requirements
1.	Create NumPy array of student marks.
2.	Reshape to 2D.
3.	Convert to Pandas DataFrame.
4.	Add missing value.
5.	Replace missing value with mean.
6.	Remove duplicate rows.
7.	Generate summary statistics.
'''
print("\nTASK 5 - Mini Data Analysis Project ")
import numpy as np
import pandas as pd
print("Mini Data Analysis Project")
marks = np.array([85, 90, 78, 89, 85, 88])
print(marks)
marks_2d = marks.reshape(3, 2)
print("\n2D Array:")
print(marks_2d)
df = pd.DataFrame(marks_2d, columns=["Maths", "Science"])
df.loc[1, "Science"] = np.nan
df["Science"] = df["Science"].fillna(df["Science"].mean())
df = df.drop_duplicates()
print("\nCleaned DataFrame:")
print(df)
print("\nSummary Statistics:")
print(df.describe())

print("======================================================================")
###############################################################################
###############################################################################
'''
Task 6: Color Theme Switcher
Create a Tkinter program that performs the following:
Requirements:
Add labels and entry box
 Create buttons:
    •	Light Mode
    •	Dark Mode
    •	Blue Theme
 Clicking buttons should change:
    •	Window background
    •	Label colors
    •	Entry colors
'''
import tkinter as tk
root = tk.Tk()
root.title("Task 6: Color Theme Switcher")
root.geometry("500x500")
def light_mode():
    root.configure(bg="white")
    l.configure(bg="white", fg="black")
    e.configure(bg="white", fg="black", insertbackground="black")

def dark_mode():
    root.configure(bg="black")
    l.configure(bg="black", fg="white")
    e.configure(bg="gray20", fg="white", insertbackground="white")

def blue_theme():
    root.configure(bg="lightblue")
    l.configure(bg="lightblue", fg="navy")
    e.configure(bg="skyblue", fg="black", insertbackground="black")
l = tk.Label(root, text="Enter something", font=("Arial", 14))
l.pack(pady=10)
e = tk.Entry(root, font=("Arial", 14), width=25)
e.pack(pady=10)
b_light = tk.Button(root, text="Light Mode", width=15, command=light_mode)
b_light.pack(pady=5)
b_dark = tk.Button(root, text="Dark Mode", width=15, command=dark_mode)
b_dark.pack(pady=5)
b_blue = tk.Button(root, text="Blue Theme", width=15, command=blue_theme)
b_blue.pack(pady=5)
root.mainloop()

print("======================================================================")
###############################################################################
###############################################################################
'''
TASK-7:The Smart Hospital Management Assistant
A modern hospital uses a Python-based assistant to manage 
daily operations smoothly.
The assistant relies on Python built-in libraries to automate 
routine tasks and reduce human effort.
Your job as a Python intern is to build this assistant.

 a. Patient Check-In Time (datetime library)
Whenever a patient arrives, the system:
    •	Records the current date and time
    •	Displays the day of the week
This helps doctors track appointment timings accurately.

 b. Doctor Assignment System (random library)
To distribute workload fairly, the system:
    •	Randomly assigns an available doctor to a patient
    •	Randomly selects a room number between 100 and 500
This prevents overcrowding.

c. Billing Calculation (math library)
The hospital calculates:
    •	Total bill amount
    •	Service tax
    •	Rounded final bill value
This ensures accurate and fair billing.

 d. Patient Record File Management (os library)
Patient records are stored as files.
The system:
    •	Checks if the patient file exists
    •	Creates a new file if not
    •	Displays confirmation message
This keeps patient data organized and secure.

e. System Status Check (sys library)
Before closing the program, the assistant:
    •	Displays Python version
    •	Shows system arguments
    •	Safely exits the application
This ensures the system runs without errors.

'''
print("\nTASK-7:The Smart Hospital Management Assistant\n")
import datetime
import random
import math
import os
import sys
print("Patient Check-In Details")
print("------------------------")
now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y")
time = now.strftime("%I:%M %p")
day = now.strftime("%A")
print(f"Date : {date}")
print(f"Time : {time}")
print(f"Day  : {day}")
print()
print("Doctor Assignment")
print("-----------------")
doctors = ["Dr. Pim", "Dr. Banner", "Dr. Strange", "Dr. Octopus"]
doctor = random.choice(doctors)
room_num = random.randint(100, 500)
print(f"Doctor Name : {doctor}")
print(f"Room Number : {room_num}")
print()
print("Billing Details")
print("---------------")
base_amount = 2200
tax_rate = 0.1
amount = base_amount * tax_rate
final = base_amount + amount
rounded_final = math.ceil(final)
print(f"Base Amount : {base_amount}")
print(f"Tax Amount  : {int(amount)}")
print(f"Final Bill  : {rounded_final}")
print()
print("Patient Record Status")
print("---------------------")
file_name = "patient_record.txt"
if os.path.exists(file_name):
    print("File exists : Yes")
    print("Updating the file\n")
else:
    print("File exists : No")
    with open(file_name, "w") as file:
        file.write("New patient record created.\n")
    print("File created successfully!")
with open(file_name, "w") as file:
        file.write("Patient Record\n")
        file.write("--------------------\n")
        file.write(f"Name : Ash\n")
        file.write(f"Age : 22\n")
        file.write(f"Check-In Date : {date}\n")
        file.write(f"Check-In Time : {time}\n")
        file.write(f"Assigned Doctor : {doctor}\n")
        file.write(f"Room Number : {room_num}\n")
        file.write(f"Final Bill : {rounded_final}\n")
with open(file_name, "r") as file:
    content = file.read()
    print(content)
print()
print("System Information")
print("------------------")
print(f"Python Version : {sys.version.split()[0]}")
print(f"System Arguments : {sys.argv}")
print("Program closed safely.")
sys.exit()