print("task 1\n")
text = "artificial intelligence"
print(text[:11]) # 1st 10 chars
print(text[-5::]) # last 5 chars
print(text[1::2]) # every 2nd char
print(text[::-1]) # reverse
print(text[11:]) # intelligence

print("======================================================================")
print("task 2\n")
email = "student@gmail.com"
print(email[:7]) # username
print(email[8:13]) # domain
print(email[-3:]) # domain extention

print("======================================================================")
print("task 3\n")
numbers = [10, 20, 30, 40, 50]
numbers.append(60)
print(numbers)
numbers.remove(30)
print(numbers)
numbers.insert(2, 25)
print(numbers)
print(f"max = {max(numbers)}, min = {min(numbers)}")
numbers.reverse()
print(numbers)

print("======================================================================")
print("task 4\n")
data = [12, 45, 67, 23, 89, 45, 12, 90]
new = []
for i in data:
    if i not in new:
        new.append(i)
print(new)
new.sort()
print(new)
new.sort(reverse = True)
print(new)

print("======================================================================")
print("task 5\n")
t = (10, 20, 30, 40, 50)
print(f"first element: {t[0]}, last element: {t[-1]}")
print(f"length of tuple = {len(t)}")
if 30 in t:
    print("30 exists in tuple")
else:
    print("30 dosent exist in tuple")
print(t)
print(list(t))

print("======================================================================")
print("task 6\n")
student = {
    "name": "Rahul",
    "age": 21,
    "marks": 85
}
print(student.keys())
print(student.values())
student["grade"] = "A"
print(student)
student["marks"] = 95
print(student)
student.pop("age")
print(student)

print("======================================================================")
print("task 7\n")
def add(x, y):
    return(print(x + y))
def odd_even(x):
    if x % 2 == 0:
        return(print(f"{x} is an even number"))
    else:
        return(print(f"{x} is an odd number"))
def fact(x):
    f = 1
    for i in range(1, x + 1):
        f *= i
    return(print(f"factorial of {x} is: {f}"))
add(5, 7)
odd_even(4)
odd_even(7)
fact(3)

print("======================================================================")
print("task 8\n")
for i in range(1, 6):
    print(f"{i}" * i)

print("======================================================================")
print("task 9\n")

num = 12345
n = num
s = 0
while num>0:
    d = num%10
    s += d
    num = num//10
print(f"sum of the digits in {n} is {s}")

print("======================================================================")
print("task 10\n")

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, age: {self.age}, marks: {self.marks}")

student1 = Student("Abdul", 23, 92)
student2 = Student("Ash", 25, 100)
student1.display()
student2.display()

print()

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_balance(self):
        print(f"Balance: {self.balance}")

account = BankAccount("112233", 50000)
dep = int(input("Enter amount to deposit: "))
account.deposit(dep)
account.display_balance()
wit = int(input("Enter amount to withdraw: "))
account.withdraw(wit)
account.display_balance()

print("======================================================================")
print("task 11\n")
import pandas as pd

data = {
    "Name": ["A", "B", "C"],
    "Age": [20, 21, 19],
    "Marks": [85, 90, 78]
}
df = pd.DataFrame(data)
print(df.head(1))
print()
print(df["Marks"])

print("======================================================================")
print("task 12\n")

import pandas as pd

df = pd.read_csv("data.csv")
print(df.head())
print(df.tail())
print(df.columns)
no_null = df.dropna()
print(no_null)
fill_null = df.fillna(df.mean(numeric_only=True))
print(fill_null)