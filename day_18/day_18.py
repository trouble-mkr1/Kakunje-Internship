print("============== PART 1 ==============")
'''
TASK-1. Digital Diary Application 
You are building a Digital Personal Diary where a user writes daily thoughts. 
1. Check if a file named diary.txt exists. 
2. If it does not exist, create the file and write at least 5 diary entries (each on a new 
line). 
3. Read and display: 
    o the entire diary 
    o only the first 50 characters 
    o the diary line by line 
4. After displaying the content, delete the diary file.
'''
print("task 1:  Digital Diary Application\n")
import os
f = "diary.txt"
# 1
if os.path.exists(f):
    print("Diary file exist!!\n")
else:
    print("Diary file dosent exist!! Creating a new diary entry\n")
    #2
    with open(f, "w") as file:
        file.write("Today was a productive day.\n")
        file.write("Not because I learnt something new,\n")
        file.write("But because I practiced writing and reading files.\n")
        file.write("I was given tasks to do file handling concepts today\n")
        file.write("This weekend is really full of learning for me!!\n")
#3
print("The Diary Contents are: ")
with open(f, "r") as file:
    print(file.read())
print("printing first 50 characters")
with open(f, "r") as file:
    print(file.read(50))
print("\nprinting diary contents line by line")
with open(f, "r") as file:
    for l in file:
        print(l.strip())
#4
os.remove(f)
print(f"\n{f} deleted")

print("======================================================================")
###############################################################################
###############################################################################
'''
Task-2:Mobile Recharge Recommendation System
A telecom company suggests recharge plans based on user budget.
• Ask the user for:
    o	mobile number
    o	budget amount
• Based on budget:
    o	₹199 → 28 days
    o	₹299 → 56 days
    o	₹499 → 84 days
• Display the recommended plan
'''
print("task 2: Mobile Recharge Recommendation System\n")
#1
m = (input("Please enter mobile number: +91 "))
if len(m) != 10 or not m.isdigit():
    print("Mobile number invalid!!")
else:
    b = int(input("Please enter your budget for recharge: "))
#2
    if(b<200):
        print(f"\nbased on budget {b}, the recharge plan is of 28 days")
    elif(b<300):
        print(f"\nbased on budget {b}, the recharge plan is of 56 days")
    else:
        print(f"\nbased on budget {b}, the recharge plan is of 84 days")

print("======================================================================")
###############################################################################
###############################################################################
'''
Task-3: Washing Machine Load Manager 
A home appliance company wants a simple program to help users decide 
if the washing machine can handle the laundry load.
• Ask the user for:
    o	type of clothes (Cotton / Wool / Synthetic)
    o	number of clothes
    o	weight per cloth (in kg)
• Calculate total load weight
• Conditions:
    o	If total weight ≤ 7 kg → “Wash Started”
    o	If total weight > 7 kg → “Overload! Reduce clothes”
• Display:
    o	clothes type
    o	total load weight
    o	washing status
'''
print("task 3: Washing Machine Load Manager\n")
st=False
#1
t=input("Enter then type of cloth(Cotton / Wool / Synthetic)")
n=int(input("number of clothes: "))
w=float(input("weight per clothes (in kg): "))
#2
tt=w*n
if(tt<=7.0):
    print("Wash Started.")
    st=True
else:
    print("Overload! Reduce clothes")
#3
print("\nWashing machine status:")
print(f"Cloth Type:{t}")
print(f"total weight:{tt}")
if(st):
    print("Wash Started.")
else:
    print("Overload!! Washing Machine wont start!!")

print("======================================================================")
###############################################################################
###############################################################################
'''
TASK-4: A bus travel company wants to store passenger ticket details. 
1. Create a class BusTicket. 
2. Use __init__ to store: 
    o passenger name 
    o bus number 
    o seat number 
3. Create two ticket objects. 
'''
print("task 4: A bus travel company wants to store passenger ticket details\n")

#1
class BusTicket:  
#2
    def __init__(self, name, bus_num, seat_num):
        self.name = name
        self.bus_num = bus_num
        self.seat_num = seat_num
#3
t1 = BusTicket("Abdul", "11", 12)
t2 = BusTicket("Ash", "99", 7)
print("Ticket 1 Details:")
print("Passenger Name:", t1.name)
print("Bus Number:", t1.bus_num)
print("Seat Number:", t1.seat_num)

print("\nTicket 2 Details:")
print("Passenger Name:", t2.name)
print("Bus Number:", t2.bus_num)
print("Seat Number:", t2.seat_num)

print("======================================================================")
###############################################################################
###############################################################################
'''
TASK-5:Pin Verification
A phone's lock PIN must be protected. 
1. Create a class Mobile. 
2. Make pin private. 
3. Create methods to: 
    o verify PIN 
    o change PIN 
4. Do not allow direct access to PIN
'''
print("task 5: Pin verification\n") 

from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def verify_pin(self, e_pin):
        pass

#1
class Mobile(Device):
    #2
    def __init__(self, pin):
        self.__pin = pin
    #3
    def verify_pin(self, e_pin):
        if e_pin == self.__pin:
            print("PIN Verified. Phone Unlocked!")
        else:
            print("Incorrect PIN!")
    
    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            print("PIN changed successfully!")
        else:
            print("Incorrect old PIN. Cannot change.")
#4
phone = Mobile("1234")
phone.verify_pin("1234")
phone.change_pin("1234", "5678")
phone.verify_pin("1234")
phone.verify_pin("5678")

print("======================================================================")
###############################################################################
###############################################################################
'''
TASK-6:Smart Travel Planner 
(use Variables, Input / Output, Arithmetic operations, Conditional statements, File handling, datetime, math, os libraries)
A travel agency wants a small Python program that helps customers plan their trip. The system should record booking time, calculate trip cost, and generate a travel confirmation file.
 Task
1.Ask the user for:
    o	Customer name
    o	Destination city
    o	Number of travelers
    o	Cost per ticket
2.Use:
    o	datetime → to show booking date and time
    o	math → round total cost
    o	os → check if confirmation file exists
3.Calculate:
    o	Total cost
    o	Add 5% service charge
4.Create a confirmation file named:
    booking.txt
5.Display:
    o	Booking time
    o	Final cost
    o	File creation status
'''
print("task 6: Smart Travel Planner\n")

import os
import datetime
#1
name = input("Enter customer name: ")
destination = input("Enter destination city: ")
n = int(input("Enter number of travelers: "))
cost = float(input("Enter cost per ticket: "))
#2
t = datetime.datetime.now()
total_cost = n * cost
s_charge = total_cost * 0.05
f_cost = total_cost + s_charge
#3
filename = "booking.txt"
if os.path.exists(filename):
    print("\nBooking file already exists, updating!!")
else:
    print("\nBooking file dosent exist!! Creating booking file")
#4
with open(filename, "w") as file:
    file.write("Travel Booking Confirmation: \n")
    file.write(f"Customer Name: {name}\n")
    file.write(f"Destination: {destination}\n")
    file.write(f"Number of Travelers: {n}\n")
    file.write(f"Booking Time: {t}\n")
    file.write(f"Final Cost: {f_cost}\n")
#5
print("\nBooking Details: ")
print("Booking Time:", t)
print("Final Cost:", f_cost)
print("Booking confirmation saved in", filename)
print(f"\nDisplaying {filename}: ")
with open(filename, "r") as file:
    print(file.read())

print("======================================================================")
###############################################################################
###############################################################################
'''
Task-7. Smart Health Check Report
(use Conditional statements,File creation, Built-in libraries, Data types, String formatting)
A clinic wants a program to generate a simple patient health report and store it in a file.
1.Ask user for:
    o	Patient name
    o	Age
    o	Body temperature
    o	Heart rate
2.Use:
    o	datetime → record check-up time
    o	sys → show Python version
    o	os → check if report file exists
3.Conditions:
    o	Temperature > 37.5 → “Fever Detected”
    o	Otherwise → “Normal”
4.Create a file:
    health_report.txt
6.Display system information before exit
'''
print("task 7: Smart Health Check Report\n")

import os
import datetime
import sys
fever = False
#1
name = input("Enter patient name: ")
age = int(input("Enter age: "))
temp = float(input("Enter Body temperature in C: "))
heart = float(input("Enter heart rate: "))
#2
t = datetime.datetime.now()
print("\nPython Version:", sys.version)
filename = "health_report.txt"
if os.path.exists(filename):
    print("\nHealth Report file already exists, updating!!")
else:
    print("\nHealth Report file dosent exist!! Creating Health Report file")
#3
if temp>37.5:
    print("\nFever detected\n")
    fever = True
else:
    print("temperature Normal\n")
#4
with open(filename, "w") as file:
    file.write("Health Report: \n")
    file.write(f"Check-up Time: {t}\n")
    file.write(f"Patient Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Body Temperature: {temp}\n")
    file.write(f"Heart rate: {heart}\n")
    file.write(f"fever detection result: {fever}\n")
#5
with open(filename, "r") as file:
    print(file.read())

print("======================================================================")
###############################################################################
###############################################################################
'''
TASK- 8. Smart Weather Analyzer
A weather monitoring center records daily temperature and generates weather reports.
1.Ask user to enter temperature for 5 days.
2.Store in a list.
3.Calculate:
    o	Maximum temperature
    o	Minimum temperature
    o	Average temperature
4.Use:
    o	math → rounding
    o	datetime → report date
    o	os → check if report file exists
5.Classify weather:
    o	Avg ≥ 35 → “Hot Week”
    o	Avg between 20-34 → “Pleasant Week”
    o	Below 20 → “Cold Week”
6.Create file:
    weather_report.txt
'''
print("task 8: Smart Weather Analyzer\n")

import os
import math
import datetime
#1
temp = []
for i in range(1, 6):
    t = float(input(f"Enter temperature for Day {i}: "))
    #2
    temp.append(t)
#3
max_temp = max(temp)
min_temp = min(temp)
avg_temp = sum(temp) / len(temp)
#4
avg_temp = math.ceil(avg_temp)
report_date = datetime.datetime.now()
filename = "weather_report.txt"

if os.path.exists(filename):
    print("\nReport file already exists. Overwriting")
else:
    print("\nCreating weather report file")
#5
if avg_temp >= 35:
    weather = "Hot Week"
elif 20 <= avg_temp <= 34:
    weather = "Pleasant Week"
else:
    weather = "Cold Week"
#6
with open(filename, "w") as file:
    file.write("Weekly Weather Report: \n")
    file.write(f"Report Date: {report_date}\n")
    file.write(f"Temperatures: {temp}\n")
    file.write(f"Maximum Temperature: {max_temp}\n")
    file.write(f"Minimum Temperature: {min_temp}\n")
    file.write(f"Average Temperature: {avg_temp}\n")
    file.write(f"Weather Classification: {weather}\n")
with open(filename, "r") as file:
    print(file.read())

print("======================================================================")
###############################################################################
###############################################################################
'''
TASK-9: Simple Calculator 
Create a Tkinter program that performs the following:
Requirements:
 Two Entry boxes for numbers
 Add buttons:
•	Add
•	Subtract
•	Multiply
•	Divide
Display result in a label.
'''
print("task 9: Simple Calculator\n")

import tkinter as tk

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
    a = int(e1.get())
    b = int(e2.get())
    r.config(text = f"Result = {a/b}")

root = tk.Tk()
root.title("calculator")
root.geometry("300x450")
root.configure(bg = "lightblue")
l1 = tk.Label(root, text = "enter first number", bg = "lightblue", fg = "red", font = ("Arial", 14))
l1.pack(pady = "10")
e1 = tk.Entry(root, bg = "lightblue", fg = "red", insertbackground="white")
e1.pack(pady = "10")
l2 = tk.Label(root, text = "enter second number", bg = "lightblue", fg = "red", font = ("Arial", 14))
l2.pack(pady = "10")
e2 = tk.Entry(root, bg = "lightblue", fg = "red")
e2.pack(pady = "10")
add_b = tk.Button(root, text = "ADD", command = add, bg = "lightblue", fg = "red", font = ("Arial", 14),
              activebackground = "green", activeforeground="yellow")
add_b.pack(pady = "10")
sub_b = tk.Button(root, text = "SUB", command = sub, bg = "lightblue", fg = "red", font = ("Arial", 14),
              activebackground = "green", activeforeground="yellow")
sub_b.pack(pady = "10")
mul_b = tk.Button(root, text = "MUL", command = mul, bg = "lightblue", fg = "red", font = ("Arial", 14),
              activebackground = "green", activeforeground="yellow")
mul_b.pack(pady = "10")
div_b = tk.Button(root, text = "DIV", command = div, bg = "lightblue", fg = "red", font = ("Arial", 14),
              activebackground = "green", activeforeground="yellow")
div_b.pack(pady = "10")
r = tk.Label(root, text = "", bg = "lightblue", fg = "red", font = ("Arial", 14))
r.pack(pady = "10")
root.mainloop()

print("======================================================================")
###############################################################################
###############################################################################
print("============== PART 2 ==============")
'''
TASK-10: A Day in the Life of a Smart City Control Room
In a smart city, there is a Central Control Room that manages daily activities using Python programs.
Every morning, the system starts working automatically and performs the following tasks using built-in Python libraries:

1. Time & Date Monitoring (datetime library)
The system records:
•	Current date
•	Current time
•	Day of the week
This helps the city know when each task was performed.

 2. Traffic Signal Simulation (random library)
To avoid traffic jams, the system randomly:
•	Chooses which road gets the green signal
•	Sets a random green-light duration between 30 and 90 seconds
This makes traffic flow dynamic and fair.

 3. Energy Consumption Analysis (math library)
The system calculates:
•	Total electricity used
•	Average daily usage
•	Rounded-off power units for billing
Mathematical operations help the city reduce energy waste.
4. Citizen Complaint Records (os library)
The city stores complaints in files.
The system:
•	Checks if the complaint file exists
•	Creates a new file if it doesn't
•	Displays file size and file name
This keeps the record system organized and safe.

 5. Daily Report Generation (sys library)
At the end of the day, the system:
•	Takes command-line input for report name
•	Prints system version details
•	Exits safely after report generation
This ensures smooth system shutdown.
'''
print("task 10: A Day in the Life of a Smart City Control Room\n")

import datetime
import random
import math
import os
import sys
print("Smart City Control Room\n")

# 1. Time & Date Monitoring
now = datetime.datetime.now()
print("Date :", now.strftime("%d-%m-%Y"))
print("Time :", now.strftime("%I:%M %p"))
print("Day  :", now.strftime("%A"), "\n")
# 2. Traffic Signal Simulation
roads = ["Road A", "Road B", "Road C"]
green = random.choice(roads)
duration = random.randint(30, 90)
print("Traffic Update:")
print("Green Signal ->", green)
print("Duration ->", duration, "seconds\n")
# 3. Energy Consumption Analysis
units = [120.5, 130.2, 140.8, 121.3]
total = sum(units)
average = total / len(units)
rounded_avg = math.ceil(average)
print("Energy Report:")
print("Total Units Used :", total)
print("Average Units :", rounded_avg, "\n")
# 4. Complaint File Check
filename = "complaints.txt"
if os.path.exists(filename):
    print("Complaint File Status:")
    print("File exists: Yes\n")
else:
    open(filename, "w").close()
    print("Complaint File Status:")
    print("File exists: No, New file created!!\n")
# 5. Daily Report Generation
if len(sys.argv) > 1:
    report_name = sys.argv[1]
else:
    report_name = "Daily_Report"
print("System Version:", sys.version)
print("System Report Generated Successfully!")
sys.exit()

print("======================================================================")
###############################################################################
###############################################################################
'''
TASK 11- Mini Data Analysis Project 
(Use NumPy arrays(1D,2D) ,reshape(), sort(), where(), Pandas, DataFrame, fillna(), drop_duplicates(), describe())
Task Requirements
1.	Create NumPy array of student marks.
2.	Reshape to 2D.
3.	Convert to Pandas DataFrame.
4.	Add missing value.
5.	Replace missing value with mean.
6.	Remove duplicate rows.
7.	Generate summary statistics.
'''
print("task 11: Mini Data Analysis Project\n")

import numpy as np
import pandas as pd

print("Mini Data Analysis Project\n")

# 1. Create NumPy 1D array of student marks
marks = np.array([85, 90, 78, 90, 85, 88])
print(marks, "\n")
# 2. Reshape to 2D
marks_2d = marks.reshape(3, 2)
print("2D Array:\n")
print(marks_2d, "\n")
# 3. Convert to Pandas DataFrame
df = pd.DataFrame(marks_2d, columns=["Maths", "Science"])
print(df, "\n")
# 4. Add missing value
df.loc[1, "Science"] = np.nan
print(df, "\n")
# 5. Replace missing value with mean
df["Science"] = df["Science"].fillna(df["Science"].mean())
print(df, "\n")
# 6. Remove duplicate rows
df = df.drop_duplicates()
print("\nCleaned DataFrame:\n")
print(df)
# 7. Generate summary statistics
print("\nSummary Statistics:\n")
print(df.describe())