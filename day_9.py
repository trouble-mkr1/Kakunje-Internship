class employee:
    company = "Kakunje"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Company: {self.company}")

emp1 = employee("Alice", 30)
emp1.display()

print("==============================================================================================")
############################################################################################################################
############################################################################################################################
"""
Task 1: Class & Object
Create a class Student with:
· Attributes: name, roll_no
· Method: display()
Create two objects and display their details.
"""
print("Task 1: Class & Object\n")
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}")

student1 = Student("Abdul", 100)
student2 = Student("Ash", 999)
student1.display()
student2.display()

print("==============================================================================================")
############################################################################################################################
############################################################################################################################
"""
Task 2: Constructor
Create a class Employee:
· Use__init__() to accept id, name, salary
· Print employee details using a method
"""
print("Task 2: Constructor\n")
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.salary}")

emp1 = Employee(101, "Alice", 50000)
emp2 = Employee(999, "Ash", 1000000)
emp1.display()
emp2.display()

print("==============================================================================================")
############################################################################################################################
############################################################################################################################
"""
Task 3: Instance vs Class Variable
Create a class College:
· Class variable: college_name
· Instance variables: student_name, branch
Display details for multiple students.
"""
print("Task 3: Instance vs Class Variable\n")
class College:
    college_name = "SCEM"

    def __init__(self, student_name, branch):
        self.student_name = student_name
        self.branch = branch

    def display(self):
        print(f"Student Name: {self.student_name}, Branch: {self.branch}, College: {self.college_name}")

student1 = College("Abdul", "Computer Science")
student2 = College("Ash", "AIML")
student1.display()
student2.display()

print("==============================================================================================")
############################################################################################################################
############################################################################################################################
"""
Task 4: Private Variable
Create a class BankAccount:
· Private variable: __balance
· Methods: deposit(), withdraw(), show_balance()
"""
print("Task 4: Private Variable\n")
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance+= amount

    def withdraw(self, amount):
        self.__balance -= amount

    def show_balance(self):
        print(f"Balance: {self.__balance}")

account = BankAccount()
dep = int(input("Enter amount to deposit: "))
account.deposit(dep)
account.show_balance()
wit = int(input("Enter amount to withdraw: "))
account.withdraw(wit)
account.show_balance()

print("==============================================================================================")
############################################################################################################################
############################################################################################################################
"""
Task 5: Single Inheritance
Create:
· Personclass → name, age
· Student class → marks
Display all details.
"""
print("Task 5: Single Inheritance\n")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}")

student = Student("Abdul", 20, 95)
student.display()

print("==============================================================================================")
############################################################################################################################
############################################################################################################################
"""
Task 6: Multilevel Inheritance
Create:
· Vehicle →start()
· Car→drive()
· ElectricCar →charge()
"""
print("Task 6: Multilevel Inheritance\n")
class Vehicle:
    def start(self):
        print("Vehicle started")
        
class Car(Vehicle):
    def drive(self):
        print("Car is being driven")

class ElectricCar(Car):
    def charge(self):
        print("Electric car is charging")

ev = ElectricCar()
ev.start()
ev.drive()
ev.charge()

print("==============================================================================================")
############################################################################################################################
############################################################################################################################
"""
Task 7: Mobile Phone
Create a class Mobile with:
· Attributes: brand, price
· Method: show_details()
Create 3 objects and display their details.
"""
print("Task 7: Mobile Phone\n")
class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_details(self):
        print(f"Brand: {self.brand}, Price: {self.price}")

mobile1 = Mobile("Apple", 999)
mobile2 = Mobile("Samsung", 1999)
mobile3 = Mobile("Google", 699)
mobile1.show_details()
mobile2.show_details()
mobile3.show_details()

print("==============================================================================================")
############################################################################################################################
############################################################################################################################
"""
Task 8: Laptop Configuration
Create a class Laptop:
· Constructor accepts ram, processor, storage
· Method to display configuration
"""
print("Task 8: Laptop Configuration\n")
class Laptop:
    def __init__(self, ram, processor, storage):
        self.ram = ram
        self.processor = processor
        self.storage = storage

    def display(self):
        print(f"RAM: {self.ram}, Processor: {self.processor}, Storage: {self.storage}")

laptop = Laptop("16GB", "Intel i7", "512")
laptop.display()

print("==============================================================================================")
############################################################################################################################
############################################################################################################################

