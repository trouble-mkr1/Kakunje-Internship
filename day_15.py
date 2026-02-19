import numpy as np
import pandas as pd

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(a)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)



b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b)

b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(b)

z = np.zeros((4, 2))
print(z)

o = np.ones((3, 5))
print(o)

arr = np.arange(1, 11, 2)
print(arr)

r = np.random.rand(3, 3)
print(r)

r = np.random.randint(3, 10, size = (3, 4)) #for randint, we have to specify the range(3, 10) for the numberrs and dimention in size
print(r)

r = np.random.randint(78, 96, size = 7)
print(r)

a = np.arange(1, 6, 1)
print(a)
print(a[3])

b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b)
print(b[1, 2])

d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(d)
print(d[1, 0, 1])

###############################################################################
###############################################################################
'''
Task 1: Employee Salary Data Analysis 
Given Data 
salaries = [25000, 30000, 28000, 32000, 29000, 31000, 27000, 35000, 26000] 
1.Create a NumPy 1D array using the given list. 
2.Convert it into a 2D array with 3 rows and 3 columns. 
3.Find: 
• Shape of the array 
• Data type of the array 
• Salary at row 2 column 1 
4. Slice: 
• Salaries from index 2 to index 6 
• Last 3 salaries 
5. Sort salaries: 
• Ascending 
• Descending 
6. Reshape the array into 1D again. 
7. Join the array with another array: 
bonus = [2000, 3000, 2500, 4000, 1500, 3500, 2800, 5000, 1800] 
Use concatenate().
'''
print("Task 1: Employee Salary Data Analysis\n")

salaries = [25000, 30000, 28000, 32000, 29000, 31000, 27000, 35000, 26000]

arr = np.array(salaries)
print(arr)

arr2 = arr.reshape(3, 3)
print(arr2)

print("Shape:", arr2.shape)
print("Data type:", arr2.dtype)
print("Salary at row 2 column 1:", arr2[1, 0])

print("Salaries index 2 to 6:", arr[2:7])
print("Last 3 salaries:", arr[-3:])

print("Ascending order:", np.sort(arr))
print("Descending order:", np.sort(arr)[::-1])

reshaped_1d = arr2.reshape(-1)
print("Reshaped to 1D:", reshaped_1d)

bonus = [2000, 3000, 2500, 4000, 1500, 3500, 2800, 5000, 1800]
bonus_arr = np.array(bonus)

array = np.concatenate((arr, bonus_arr))
print("Concatenated array:", array)

print("======================================================================")
###############################################################################
###############################################################################
'''
Task 2: Product Stock Management 
Given Data 
stock = [45, 60, 30, 80, 55, 90, 20, 70] 
1.Create: 
• Array of zeros (size 8) 
• Array of ones (size 8) 
• Array using arange() from 10 to 50 with step 5 
2. Convert stock into 2D array (4 rows, 2 columns). 
3.Access: 
• Element at row 3 column 1 
• First row completely 
4.Use slicing: 
• Elements from index 1 to 5 
• Elements from index -4 to -1 
5.Search: 
• Find index where stock is 90 
• Find all values greater than 50 
6. Split array using: 
• split() into 4 parts 
• hsplit() 
• vsplit()
'''
print("task 2: Product Stock Management\n")

stock = [45, 60, 30, 80, 55, 90, 20, 70]
stock_arr = np.array(stock)

zero = np.zeros(8)
one = np.ones(8)
arange = np.arange(10, 50, 5)
print(zero)
print(one)
print(arange)

stock_2d = stock_arr.reshape(4, 2)
print(stock_2d)

print("Element at row 3 column 1:", stock_2d[2, 0])
print("First row:", stock_2d[0])

print("Index 1 to 5:", stock_arr[1:6])
print("Index -4 to -1:", stock_arr[-4:-1])

print("Index where stock is 90:", np.where(stock_arr == 90)[0])
print("Values greater than 50:", stock_arr[stock_arr > 50])

print("Split into 4 parts:", np.split(stock_arr, 4))
print("HSplit:", np.hsplit(stock_2d, 2))
print("VSplit:", np.vsplit(stock_2d, 2))

print("======================================================================")
###############################################################################
###############################################################################
'''
Task 3: Temperature Monitoring System 
Given Data 
temperature = [30, 32, 31, 29, 35, 36, 33, 34, 28, 27, 26, 25] 
1. Create 1D NumPy array. 
2. Convert into 3D array: 
• 2 blocks 
• 2 rows 
• 3 columns 
3. Access: 
• First block, second row, third column 
4. Check: 
• Data type 
• Change datatype to float 
5. Slice: 
• Index 3 to 8 
• Every second value 
6. Sort: 
• Ascending 
• Descending 
7.Reshape into 4x3 matrix.
'''
print("Task 3: Temperature Monitoring System\n")

temperature = [30, 32, 31, 29, 35, 36, 33, 34, 28, 27, 26, 25]

temp_arr = np.array(temperature)
print(temp_arr)

temp_3d = temp_arr.reshape(2, 2, 3)
print("3D Array:\n", temp_3d)

print("First block, second row, third column:", temp_3d[0, 1, 2])

print("Data type:", temp_arr.dtype)
temp_float = temp_arr.astype(float)
print("Changed to float:", temp_float.dtype)

print("Index 3 to 8:", temp_arr[3:9])
print("Every second value:", temp_arr[::2])

print("Ascending:", np.sort(temp_arr))
print("Descending:", np.sort(temp_arr)[::-1])

temp_4x3 = temp_arr.reshape(4, 3)
print("4x3 Matrix:\n", temp_4x3)

print("======================================================================")
###############################################################################
###############################################################################
'''
Task 4: Student Roll Number Processing 
Given Data 
roll_numbers = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110] 
1. Create array using arange() from 101 to 111. 
2. Create: 
• Zeros array (size 10) 
• Ones array (size 10) 
3. Convert roll_numbers into 2D array (5 rows, 2 columns). 
4.Join roll_numbers with: 
extra_roll = [111, 112, 113, 114, 115] 
5. Search: 
• Find index of 105 
• Find roll numbers greater than 107 
6. Split joined array into 3 equal parts. 
7. Check shape before and after reshaping
'''
print("Task 4: Student Roll Number Processing\n")

roll_numbers = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]

arr = np.arange(101, 111)
print("Arange array:", arr)

zeros_arr = np.zeros(10)
ones_arr = np.ones(10)
print("Zeros:", zeros_arr)
print("Ones:", ones_arr)

roll_arr = np.array(roll_numbers)
roll_2d = roll_arr.reshape(5, 2)
print("2D Array:\n", roll_2d)

extra_roll = np.array([111, 112, 113, 114, 115])
joined = np.concatenate((roll_arr, extra_roll))
print("Joined array:", joined)

print("Index of 105:", np.where(joined == 105)[0])
print("Roll numbers > 107:", joined[joined > 107])

split_arr = np.split(joined, 3)
print("Split into 3 parts:", split_arr)

print("Shape before reshape:", roll_arr.shape)
reshaped = roll_arr.reshape(2, 5)
print("Shape after reshape:", reshaped.shape)

print("======================================================================")
###############################################################################
###############################################################################