'''
Task 1: File Manager System
Write a Python program that performs the following operations:
1. Create a folder named “Intern_Data”.
2. Inside that folder, create a file named “info.txt".
3. Write your Name and Course inside the file.
4. Check whether the file exists or not.
5. Display the current working directory.
6. List all files inside the “Intern_Data" folder.
7. Display the operating system type.
8. Rename the file from info.txt to student_info.txt.
'''
# print("Task 1: File Manager System\n")
# import os
# folder_name = "Intern_Data"
# file_name = "info.txt"


# os.makedirs(folder_name)
# file_path = os.path.join(folder_name, file_name)
# with open(file_path, 'w') as file:
#     file.write("Name: Abdul\nCourse: Python Programming")
# if os.path.exists(file_path):
#     print(f"{file_name} exists.")
# print("Current Working Directory:", os.getcwd())
# print("Files in Intern_Data folder:", os.listdir(folder_name))
# print("Operating System Type:", os.name)
# new_file_name = "student_info.txt"
# new_file_path = os.path.join(folder_name, new_file_name)
# os.rename(file_path, new_file_path)
# print(f"File renamed to {new_file_name}")

print("==============================================================================================")
############################################################################################################################
############################################################################################################################
'''
Task 2: Simple Argument Printer (using sys module)
Write a Python program that performs the following operations:
1. Print the script name using sys.argv.
2. Print all command-line arguments entered.
3. Print the Python version.
4. Take user input using standard input.
5. Display a welcome message using the entered name.
6. Display output using standard output.
'''
print("Task 2: Simple Argument Printer\n")

import sys
print("Script Name:", sys.argv[0])
print("Command-line Arguments:", sys.argv[1:])
print("Python Version:", sys.version)
name = input("Enter your name: ")
print(f"Welcome, {name}!")
print("Hello people")

print("==============================================================================================")
############################################################################################################################
############################################################################################################################
'''
Task 3: Copy File Program (using shutil module)
Write a program that:
1. Copies a file named "sample.txt".
2. Pastes it as "copy_sample.txt".
3. Prints disk usage.
'''
print("Task 3: Copy File Program\n")

import shutil
a = "sample.txt"
b = "copy_sample.txt"
shutil.copy(a, b)
total, used, free = shutil.disk_usage(".")
print(f"Total: {total // (2**30)} GB")
print(f"Used: {used // (2**30)} GB")
print(f"Free: {free // (2**30)} GB")

print("==============================================================================================")
#############################################################################################################################
#############################################################################################################################
'''
Task 4: Dice and Card Simulator
Write a Python program that performs the following operations:
1. Generate a random number between 1 and 6 (like rolling a dice).
2. Print the dice result.
3. Create a list of cards: ["Ace", "King", "Queen", "Jack"].
4. Shuffle the cards randomly.
5. Generate and print one random card from the shuffled list.
'''
print("Task 4: Dice and Card Simulator\n")

import random
x = random.randint(1, 6)
print(f"Dice Shows: {x}")
cards = ["Ace", "King", "Queen", "Jack"]
random.shuffle(cards)
y = random.choice(cards)
print(f"Random Card: {y}")

print("==============================================================================================")
############################################################################################################################
############################################################################################################################
'''
Task 5: Number Operations (using math module)
Write a program that:
1. Takes a number from user.
2. Prints:
   - Square root
   - Factorial
   - Floor value
   - Ceiling value
'''
print("Task 5: Number Operations\n")

import math
n = int(input("Enter a number: "))
print(f"Square Root: {math.sqrt(n)}")
print(f"Factorial: {math.factorial(n)}")
print(f"Floor Value: {math.floor(n)}")
print(f"Ceiling Value: {math.ceil(n)}")

print("==============================================================================================")
############################################################################################################################
############################################################################################################################
'''
Task 6: Student Performance Analyzer (using statistics module)
Write a Python program that performs the following operations:
1. Create a list of student marks (example: 78, 85, 92, 88, 76).
2. Calculate the average of the marks.
3. Calculate the median of the marks.
4. Calculate the standard deviation of the marks.
5. Display all calculated results clearly.
'''
print("Task 6: Student Performance Analyzer\n")

import statistics
marks = [78, 85, 92, 88, 76]
average = statistics.mean(marks)
median = statistics.median(marks)
std_dev = statistics.stdev(marks)
print(f"Marks: {marks}")
print(f"Average: {average}")
print(f"Median: {median}")
print(f"Standard Deviation: {std_dev}")

print("==============================================================================================")
############################################################################################################################
############################################################################################################################
'''
Task 7: Store Location and College Data (using json module)
Write a Python program that performs the following operations:
1. Take location and college name as input from the user.
2. Store the data in a JSON file named data.json.
3. Read the data from the JSON file.
4. Print the stored data clearly.
'''
print("Task 7: Store Location and College Data\n")
import json
loc = input("Enter your location: ")
college = input("Enter your college name: ")
data = {
    "location": loc,
    "college": college
}
with open("data.json", "w") as f:
    json.dump(data, f)
with open("data.json", "r") as f:
    loaded_data = json.load(f)
print(f"Stored Data: {loaded_data}")

print("==============================================================================================")
############################################################################################################################
############################################################################################################################

