'''
task 1:
1. Write a function to multiply two numbers and return the result and
print it in the function call.
2. Create a function to check whether a number is even or odd.
3. Write a function to find the maximum of three numbers.
4. Create a function to calculate the factorial of a number.
5. Write a function to count vowels in a given string.
6. Define a function to reverse a string.
7. Write a function to check if a number is prime.
8. Write a function using default arguments.
9. Create a function using keyword arguments.
10. Write a recursive function to calculate Fibonacci series.
11.Write a lambda function to find the square of a number
'''
print("task 1 output\n")

def multiply(a, b):
    return a * b
print(multiply(5, 3))
def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(even_odd(10))
def max_of_three(a, b, c):
    return max(a, b, c)
print(max_of_three(5, 10, 3))
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
print(count_vowels("Internship"))
def reverse_string(s):
    return s[::-1]
print(reverse_string("Python"))
def prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(prime(7))
def add(a, b=10):
    return a + b
print(add(5))
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
print(greet(name="Alice", greeting="Hi"))
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        series = fibonacci(n - 1)   # recursive call
        series.append(series[-1] + series[-2])
        return series
print(fibonacci(10))
square = lambda x: x * x
print(square(5))
# def fibonacci(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
#     else:
#         series = [0, 1]
#         for i in range(2, n):
#             next = series[i-1] + series[i-2]
#             series.append(next)
#         return series
print("==============================================================================================")
##########################################################################################################################
##########################################################################################################################
'''
task 2: error handling
 Handle ZeroDivisionError.
· Handle ValueError when converting input to integer.
· Write a program using try and except.
· Write a program using try, except, else.
· Write a program using try, except, finally.
· Handle TypeError.
· Handle multiple exceptions in a single try block.
· Raise an exception using raise keyword
'''
print("task 2 output\n")
try:
    x = 10 / 0
except ZeroDivisionError:
    print("cannot divide by 0")
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid!! enter an integer.")
try:
    x = int(input("enter 1st number: "))
    y = int(input(f"Enter 2nd number to divide with {x}: "))
    res = x / y
except ZeroDivisionError:
    print("cannot divide by 0")
except ValueError:
    print("Invalid!! enter an integer.")
else:
    print(f"Result: {res}")
finally:
        print("task completed.")
try:
    x = 10 + "5"
except TypeError:
    print("Cannot add int and str")
try:
    num = [10, 20, 30]
    index = int(input("Enter index: "))
    print("Value:", num[index])
except IndexError:
    print("Index out of range")
except ValueError:
    print("Please enter a valid integer")
age = int(input("Enter your age: "))
if age < 18:
    raise Exception("You must be at least 18 years old to vote")
print("possible to vote")

print("==============================================================================================")
##########################################################################################################################
##########################################################################################################################
