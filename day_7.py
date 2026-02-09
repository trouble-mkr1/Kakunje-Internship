'''
Task 1: Operators Tasks

1. Calculate sum, difference, product, quotient of two numbers
2. Find remainder of division
3. Calculate simple interest
4. Convert minutes to hours and minutes
5. Find square and cube of a number
6. Check if a student passed (marks >= 40)
7. Compare two ages and print who is older
8. Check if number >= 100
9. Check if number is positive OR zero
10. Check if number is NOT negative
'''
x = 15
y = 3
print(x + y) # sum
print(x - y) # difference
print(x * y) # product
print(x / y) # quotient
print(x % y) # remainder
p, t, r = 1000, 2, 5
si = (p * t * r) / 100
print(si) # simple interest
min = 125
hrs = min // 60
min = min % 60
print(f"{hrs} hours and {min} minutes") #hours and minutes
num = 4
print(num ** 2) # square
print(num ** 3) # cube
marks1 = 35
marks2 = 75
print(marks1 >= 40) # check pass
print(marks2 >= 40) # check pass
age1 = 25
age2 = 30
if age1 > age2:
    print("age1 is older")
else:
    print("age2 is older")
num = 150
print(num >= 100) # check if number >= 100
num = -5
print(num >= 0) # check if number is positive OR zero
print(num < 0) # check if number is NOT negative

print("==============================================================================================")
##########################################################################################################################
##########################################################################################################################
'''
Task 2: Conditional Statements

1. Find the smallest of two numbers
2. Check if a person is eligible to vote
3. Check if a number is even or odd
4. Grade a student based on marks:
   >=90 : A
   >=75 : B
   >=50 : C
   Else : Fail
'''
num1 = 10
num2 = 20
if num1 < num2:
    print(f"{num1} is smaller")
else:
    print(f"{num2} is smaller")
age = 18
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
marks = [85, 65, 45]
for mark in marks:
    if mark >= 90:
        print("Grade A")
    elif mark >= 75:
        print("Grade B")
    elif mark >= 50:
        print("Grade C")
    else:
        print("Fail")

print("==============================================================================================")
##########################################################################################################################
##########################################################################################################################
'''
Task 3: Loop Tasks
(for loop)
1. Print numbers from 1 to 10
2. Print even numbers from 1 to 50
3. Print multiplication table of a number
4. Print characters of a string one by one
5. Calculate the sum of first N numbers
6. Count vowels in a string

(while loop)
7. Print numbers from 10 to 1 (while loop)
8. Find sum of digits of a number
9. Count number of digits
'''
nums = []
for i in range(1, 11):
    nums.append(i)
print(nums)
nums = []
for i in range(1, 51):
    if i % 2 == 0:
        nums.append(i)
print(nums)
num = 5
nums = []
for i in range(1, 11):
    nums.append(num * i)
print(nums)
string = "internship"
for char in string:
    print(char)
N = int(input("Enter N: "))
sum = 0
for i in range(1, N+1):
    sum += i
print(sum)
v = "aeiouAEIOU"
count = 0
for char in string:
    if char in v:
        count += 1
print(count)
print("\n")
i = 10
while i >= 1:
    print(i)
    i -= 1
num = int(input("Enter a number: "))
sum = 0
count = 0
while num > 0:
    digit = num % 10
    sum += digit
    count += 1
    num //= 10
print(sum)
print(count)

print("==============================================================================================")
##########################################################################################################################
##########################################################################################################################
