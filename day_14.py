'''
Task 1: Employee Data (CSV Module)   
The company stores employee information in a CSV file. 
Requirements: 
• Create a file named: 
    employee_data.csv 
• Add header: 
    Name, Age, Department 
• Add at least 3 employee records 
• Read and display all data from the CSV file 
• Create another CSV file using dictionaries 
(csv.DictWriter) 
'''
print("Task 1: Employee Data (CSV Module)\n")

import csv
with open("employee_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Department"])
    writer.writerow(["Abdul", "23", "IT"])
    writer.writerow(["Ash", "30", "Finance"])
    writer.writerow(["Sohan", "28", "HR"])
print("Employee Data Written Successfully!")
print("Reading employee_data.csv...\n")
with open("employee_data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row) 
data = [
    {'Name': 'Abdul', 'Age': 23, 'Department': 'IT'},
    {'Name': 'Ash', 'Age': 30, 'Department': 'Finance'},
    {'Name': 'Sohan', 'Age': 28, 'Department': 'HR'}
]
with open('employee_dict.csv', mode='w', newline='') as file:
    fieldnames = ['Name', 'Age', 'Department']
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(data)
print("Dictionary CSV file created successfully!")

# with open("employee_dict.csv", "w", newline="") as file:
#     fieldnames = ["Name", "Age", "Department"]
#     writer = csv.DictWriter(file, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow({"Name": "Abdul", "Age": "23", "Department": "IT"})
#     writer.writerow({"Name": "Ash", "Age": "30", "Department": "Finance"})
#     writer.writerow({"Name": "Sohan", "Age": "28", "Department": "HR"})

# print("\nDictionary CSV file created successfully!")

# data = [
#     {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
#     {'Name': 'Bob', 'Age': 30, 'City': 'Los Angeles'},
#     {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}
# ]

print("======================================================================")
###############################################################################
###############################################################################
'''
Task 2: Date and Time Record
Whenever the program runs, display: 
• Current date 
• Current time 
• Year, month, and day separately 
• Formatted date & time 
Use the datetime module.
'''
print("Task 2: Date and Time Record\n")

import datetime

date_time = datetime.datetime.now()
print("System Date:", date_time.date())
print("System Time:", date_time.time())

print("year: ", date_time.year)  
print("month: ", date_time.month) 
print("day: ", date_time.day)  

print("formatted_date: ", date_time.strftime("%Y-%m-%d %H:%M:%S"))

print("======================================================================")
###############################################################################
###############################################################################
'''
Task 3: System Time Tracking (Time Module)
The manager wants to see execution timing.

Requirements:
• Display current timestamp
• Show readable current time
• Wait for 2 seconds before continuing
'''
print("Task 3: System Time Tracking\n")

import time

print("Current Timestamp:", time.time())
print("Readable Time:", time.ctime())
print("\nWaiting for 2 seconds...")
time.sleep(2)
print("Continuing execution...")

print("======================================================================")
###############################################################################
###############################################################################
'''
Task 4: Data Backup (Compression)
At the end of the day, files must be backed up.

Requirements:
• Create: backup.zip
• Create: backup.tar.gz
• Add CSV files into both archives
• Display list of files inside archives
'''
print("Task 4: Data Backup\n")

import zipfile
import tarfile

print("Creating backup.zip...")
with zipfile.ZipFile("backup.zip", "w") as zipf:
    zipf.write("employee_data.csv")
    zipf.write("employee_dict.csv")

print("Creating backup.tar.gz...")
with tarfile.open("backup.tar.gz", "w:gz") as tar:
    tar.add("employee_data.csv")
    tar.add("employee_dict.csv")

print("\nFiles inside backup.zip:")
with zipfile.ZipFile("backup.zip", "r") as zipf:
    print(zipf.namelist())

print("\nFiles inside backup.tar.gz:")
with tarfile.open("backup.tar.gz", "r:gz") as tar:
    print(tar.getnames())

print("\nBackup completed successfully!")

print("======================================================================")
###############################################################################
###############################################################################
'''
Task 5: Background Backup (Threading)
The company runs backups in the background.

Requirements:
• Create a thread that prints:
  Backup running in background...
  every 2 seconds.
• The main program should continue executing normally.
'''
print("Task 5: Background Backup (Threading)\n")

import threading
import time

def backup():
    for i in range(3):
        print("Backup running in background...", i)
        time.sleep(2)

backup_thread = threading.Thread(target=backup)
backup_thread.start()

print("Main program continues working...\n")

backup_thread.join()

print("Main thread finished!")
print("Program Completed Successfully!")

print("======================================================================")
###############################################################################
###############################################################################
