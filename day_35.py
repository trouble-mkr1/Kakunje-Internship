# task 1

import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "Employee": [],
    "Salary": []
    }

def analyze():
    
    name = e1.get()
    salary = int(e2.get())
    data["Employee"].append(name)
    data["Salary"].append(salary)
    df = pd.DataFrame(data)
    avg = np.mean(df["Salary"])
    high = np.max(df["Salary"])
    low = np.min(df["Salary"])
    res.config(text=f"Average: {avg}\nHighest: {high}\nLowest: {low}")
    plt.bar(df["Employee"], df["Salary"])
    plt.title("Employee Salary Distribution")
    plt.show()

root=tk.Tk()
root.title("Task 1: Employee Salary Analyzer")
root.geometry("300x300")
tk.Label(root,text="Employee Name").pack()
e1=tk.Entry(root)
e1.pack()
tk.Label(root,text="Salary").pack()
e2=tk.Entry(root)
e2.pack()
tk.Button(root,text="Analyze",command=analyze).pack()
res=tk.Label(root,text="")
res.pack()
root.mainloop()

##############################################################
##############################################################

# Task 2

data={
    "Month":[],
    "Units":[]
    }

def analyze():
    m=month.get()
    u=int(units.get())
    data["Month"].append(m)
    data["Units"].append(u)
    df=pd.DataFrame(data)
    total=np.sum(df["Units"])
    avg=np.mean(df["Units"])
    bill=u*7
    res.config(text=f"Total Units:{total}\nAverage:{avg}\nBill:{bill}")
    plt.plot(df["Month"],df["Units"])
    plt.title("Electricity Bill Analyzer")
    plt.show()

root=tk.Tk()
root.title("Task 2: Electricity Bill Analyzer")
root.geometry("300x300")
tk.Label(root,text="Month").pack()
month=tk.Entry(root)
month.pack()
tk.Label(root,text="Units").pack()
units=tk.Entry(root)
units.pack()
tk.Button(root,text="Analyze",command=analyze).pack()
res=tk.Label(root,text="")
res.pack()
root.mainloop()

##############################################################
##############################################################

# Task 3

data={
    "Day":[],
    "Steps":[]
    }

def analyze():
    d=day.get()
    s=int(steps.get())
    data["Day"].append(d)
    data["Steps"].append(s)
    df=pd.DataFrame(data)
    avg=np.mean(df["Steps"])
    res.config(text=f"Average Steps:{avg}")
    plt.plot(df["Day"],df["Steps"],marker="o")
    plt.title("Fitness Activity Tracker")
    plt.show()

root=tk.Tk()
root.title("Task 3: Fitness Activity Tracker")
root.geometry("300x300")
tk.Label(root,text="Day").pack()
day=tk.Entry(root)
day.pack()
tk.Label(root,text="Steps").pack()
steps=tk.Entry(root)
steps.pack()
tk.Button(root,text="Track",command=analyze).pack()
res=tk.Label(root,text="")
res.pack()
root.mainloop()

##############################################################
##############################################################

# Task 4

data={
    "Student":[],
    "Attendance":[]
    }

def analyze():
    name=e1.get()
    total=int(e2.get())
    attend=int(e3.get())
    percent=(attend/total)*100
    data["Student"].append(name)
    data["Attendance"].append(percent)
    df=pd.DataFrame(data)
    avg=np.mean(df["Attendance"])
    res.config(text=f"Attendance %: {percent}\nAverage:{avg}")
    plt.bar(df["Student"],df["Attendance"])
    plt.title("Attendance Percentage")
    plt.show()

root=tk.Tk()
root.title("Task 4: Attendance Analyzer")
root.geometry("300x300")
tk.Label(root,text="Student Name").pack()
e1=tk.Entry(root)
e1.pack()
tk.Label(root,text="Total Classes").pack()
e2=tk.Entry(root)
e2.pack()
tk.Label(root,text="Classes Attended").pack()
e3=tk.Entry(root)
e3.pack()
tk.Button(root,text="Analyze",command=analyze).pack()
res=tk.Label(root,text="")
res.pack()
root.mainloop()

print("=====================================================")
##############################################################
##############################################################

# Task 5

data = {
    "Player": [],
    "Score": []
    }

n = int(input("Enter number of players: "))
for i in range(n):
    player = input("Enter player name: ")
    score = int(input("Enter score: "))
    data["Player"].append(player)
    data["Score"].append(score)
df = pd.DataFrame(data)
avg = np.mean(df["Score"])
highest = np.max(df["Score"])
print("Average Score:", avg)
print("Highest Score:", highest)
plt.bar(df["Player"], df["Score"])
plt.title("Cricket Score Analyzer")
plt.xlabel("Player")
plt.ylabel("Score")
plt.show()

print("=====================================================")
##############################################################
##############################################################

# Task 6

data = {
    "Day": [],
    "Week": [],
    "Water": []
    }
n = int(input("Enter number of days: "))
for i in range(n):
    day = input("Enter day: ")
    water = float(input("Enter water intake: "))
    week = (i // 7) + 1
    data["Day"].append(day)
    data["Week"].append(week)
    data["Water"].append(water)
df = pd.DataFrame(data)
avg = np.mean(df["Water"])
print("\nDataset:")
print(df)
print("\nAverage Water Intake:", avg)
plt.plot(df["Day"], df["Water"], marker="o")
plt.title("Daily Water Intake")
plt.xlabel("Day")
plt.ylabel("Liters")
plt.show()