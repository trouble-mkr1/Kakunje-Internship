'''
1. Website Visit Analyzer
Tasks
· Enter page name & visit count
· Store data using Pandas
· Calculate total visits (NumPy)
· Display pie chart of visits distribution
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

page = []
visit = []
while True:
    p = input("Enter page name: ")
    page.append(p)
    v = int(input(f"Enter number of visit for {p} page: "))
    visit.append(v)
    e = input("Exit?(y/n): ")
    print()
    if e == "y":
        break

df = pd.DataFrame({
    "Page": page,
    "Visits": visit
})
print("\nData Frame: \n", df)
print("\nTotal page visits: ", np.sum(visit))
plt.figure()
plt.pie(df["Visits"], labels=df["Page"], autopct='%1.1f%%')
plt.title("Task 1: Website Visit Analyzer")
plt.show()

'''
2. Delivery Time Tracker
Tasks
· Enter order ID & delivery time
· Store in Pandas
· Calculate average delivery time (NumPy)
· Show line graph
'''
id = []
time = []
while True:
    o = input("Enter Order ID: ")
    id.append(o)
    t = float(input("Enter delivery time: "))
    time.append(t)
    e = input("Exit?(y/n): ")
    print()
    if e == "y":
        break

df = pd.DataFrame({
    "ID": id,
    "Time": time
})

print("\nData Frame: \n", df)
print("\nAverage Delivery Time:", np.mean(time))
plt.plot(df["ID"], df["Time"], marker='o')
plt.title("Task 2: Delivery Time Tracker")
plt.xlabel("Order ID")
plt.ylabel("Time")
plt.show()

'''
3. Employee Salary Analyzer
Tasks
•	Enter employee name & salary
•	Store in Pandas
•	Calculate:
o	Total salary expense (NumPy)
o	Average salary
•	Show bar chart of salaries
'''
name = []
salary = []
while True:
    n = input("Enter Name: ")
    name.append(n)
    s = float(input(f"Enter salary for {n}: "))
    salary.append(s)
    e = input("Exit?(y/n): ")
    print()
    if e == "y":
        break

df = pd.DataFrame({
    "Name": name,
    "Salary": salary
})

print("\nData Frame: \n", df)
print("\nTotal salary expense:", np.sum(salary))
print("Average salary:", np.mean(salary))
plt.bar(df["Name"], df["Salary"])
plt.title("Task 3: Employee Salary Analyzer")
plt.xlabel("Name")
plt.ylabel("Salary")
plt.show()


'''
4. Product Price Comparison
Tasks
•	Enter product name & price
•	Store in Pandas
•	Calculate:
o	Highest & lowest price (NumPy)
o	Average price
•	Show comparison graph
'''
name = []
price = []
while True:
    n = input("Enter Product Name: ")
    name.append(n)
    p = float(input(f"Enter price for {n}: "))
    price.append(p)
    e = input("Exit?(y/n): ")
    print()
    if e == "y":
        break

df = pd.DataFrame({
    "Name": name,
    "Price": price
})

print("\nData Frame: \n", df)
print("\nHighest Price:", np.max(price))
print("Lowest Price:", np.min(price))
print("Average price:", np.mean(price))
plt.plot(df["Name"], df["Price"], marker = "o")
plt.title("Task 4: Product Price Comparison")
plt.show()


'''
5. Rainfall Data Analyzer
Tasks
•	Enter rainfall per day/week
•	Store data (Pandas)
•	Calculate:
o	Total rainfall (NumPy)
o	Average rainfall
•	Display line chart
'''
day = []
rain = []
while True:
    d = input("Enter Day: ")
    day.append(d)
    r = int(input(f"Enter if rained(0/1) on {d}: "))
    rain.append(r)
    e = input("Exit?(y/n): ")
    print()
    if e == "y":
        break

df = pd.DataFrame({
    "Day": day,
    "Rain": rain
})

print("\nData Frame: \n", df)
print("\nNumber of days rained: ", np.sum(rain))
print("Average rainfall: ", np.mean(rain))
plt.plot(df["Day"], df["Rain"], marker = "o")
plt.title("Task 5: Rainfall Data Analyzer")
plt.show()



'''
6. Electricity Usage Tracker
Tasks
•	Enter daily electricity units
•	Store in Pandas
•	Calculate:
o	Total usage (NumPy)
o	Average usage
•	Show usage graph
'''
day = []
units = []
while True:
    d = input("Enter Day: ")
    day.append(d)
    u = float(input(f"Enter units consumed on {d}: "))
    units.append(u)
    e = input("Exit?(y/n): ")
    print()
    if e == "y":
        break

df = pd.DataFrame({
    "Day": day,
    "Units": units
})

print("\nData Frame: \n", df)
print("\nTotal units consumed: ", np.sum(units))
print("Average units consumed: ", np.mean(units))
plt.bar(df["Day"], df["Units"])
plt.title("Task 6: Electricity Usage Tracker")
plt.show()


'''
7. Mobile Usage Analyzer
Tasks
•	Enter app name & usage time
•	Store using Pandas
•	Calculate:
o	Total screen time (NumPy)
o	Most used app
•	Display pie chart
'''

app = []
time = []
while True:
    a = input("Enter app name: ")
    app.append(a)
    t = float(input(f"Enter time spent on {a}: "))
    time.append(t)
    e = input("Exit?(y/n): ")
    print()
    if e == "y":
        break

df = pd.DataFrame({
    "App": app,
    "Time": time
})

print("\nData Frame: \n", df)
print("\nTotal screen time: ", np.sum(time))
x = time.index(max(time))
print("Most used app: ", app[x])
plt.pie(df["Time"], labels = df["App"])
plt.title("Task 7: Mobile Usage Analyzer")
plt.show()


'''
8. Sales Performance Tracker
Tasks
•	Enter product & sales amount
•	Store in Pandas
•	Calculate:
o	Total sales (NumPy)
o	Best-selling product
•	Display bar chart
'''
product = []
sales = []
while True:
    p = input("Enter product name: ")
    product.append(p)
    s = float(input(f"Enter sales amount of {p}: "))
    sales.append(s)
    e = input("Exit?(y/n): ")
    print()
    if e == "y":
        break

df = pd.DataFrame({
    "Product": product,
    "Sales": sales
})

print("\nData Frame: \n", df)
print("\nTotal sales: ", np.sum(sales))
x = sales.index(max(sales))
print("Best selling product: ", product[x])
plt.bar(df["Product"], df["Sales"])
plt.title("Task 8: Sales Performance Tracker")
plt.show()


'''
9. Disease Prediction Analyzer
· Enter confusion matrix values:
•	True Positive (TP)   •	True Negative (TN) 
•	False Positive (FP)  •	False Negative (FN) 
· Store data using Pandas
· Calculate using NumPy:
•	Accuracy   •	Precision 
•	Recall     •	F1-score 
· Display confusion matrix as table or heatmap
Given Confusion Matrix
	Actual Disease	Actual No Disease
Predicted Yes	70	20
Predicted No	10	50
Find
•	Accuracy   •	Precision 
•	Recall     •	F1-score 
'''
tp = int(input("Enter True Positive (TP): "))
tn = int(input("Enter True Negative (TN): "))
fp = int(input("Enter False Positive (FP): "))
fn = int(input("Enter False Negative (FN): "))

df = pd.DataFrame({
    "Actual Positive": [tp, fn],
    "Actual Negative": [fp, tn]
}, index=["Predicted Positive", "Predicted Negative"])
print("\nConfusion Matrix:\n")
print(df)

values = np.array([tp, tn, fp, fn])
acc = (tp + tn) / np.sum(values)
prec = tp / (tp + fp)
recall = tp / (tp + fn)
f1 = (2 * prec * recall) / (prec + recall)
print("Accuracy:", acc)
print("Precision:", prec)
print("Recall:", recall)
print("F1 Score:", f1)
