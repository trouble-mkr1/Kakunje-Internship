import matplotlib.pyplot as plt
import numpy as np
# the plot() it to draw points, it draws a line between points.
x = np.array([3, 9])
y = np.array([2, 10])
# plt.plot(x, y) # this will draw a line from x to y
plt.plot(x, y, 'o') # this will only show thw points of x and y without a line connecting them
plt.plot(x, y, marker = 'o') # this will give both lines and points
plt.show()

x = np.array([3, 9, 2, 7, 15, 3])
y = np.array([2, 10, 16, 7, 3, 10])
plt.plot(x, y)
plt.show()

a = np.array([5, 15, 10, 20])
plt.plot(a)
plt.show()

x = np.array([2, 4, 6, 8, 10, 12])
y = np.array([10, 5, 2, 6, 1, 16])
plt.plot(x, y, 'g:*') # 'g' is green color line, ':' is dotted line and '*' is star markers
plt.plot(x, y, "|--c") # the order dosent matter. here, '|' is the marker, '--' is the line style and 'c' is color
plt.show()

x = np.array([2, 4, 6, 8, 10, 12])
y = np.array([10, 5, 2, 6, 1, 16])
plt.plot(x, y)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Title example", loc = "right")
plt.show()

x = np.random.randint(100, size = (100))
y = np.random.randint(100, size = (100))
colors = np.random.randint(100, size = (100))
size = np.random.randint(100, size = (100))
plt.scatter(x, y, c = colors, s = size, cmap = "winter", alpha = 0.2)
plt.colorbar()
plt.show()

x = np.array([40, 20, 15, 15, 10])
l = np.array(["rent", "education", "emi", "grocery", "medicine"])
e = np.array([0, 0.2, 0, 0, 0])
c = np.array([])

'''
Task 1: Simple Line Plot
Create a line plot for the following data:
x = [1,2,3,4,5]
y = [10,20,30,40,50]
Requirements:
•	Add title: "Simple Line Plot"
•	Label X-axis and Y-axis
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([10,20,30,40,50])
plt.plot(x, y)
plt.title("Task 1: Simple Line Plot")
plt.show()

'''
Task 2: Plot Student Marks
Plot marks of 5 students:
students = ["A","B","C","D","E"]
marks = [75,85,60,90,70]
Requirements:
•	Line plot
•	Marker = circle
•	Color = green
•	Add title
'''
students = np.array(["A","B","C","D","E"])
marks = np.array([75,85,60,90,70])
plt.plot(students, marks, "g-o")
plt.title("Task 2: Plot Student Marks")
plt.show()

'''
Task 3: Bar Chart
Create a bar chart for:
subjects = ["Math", "Science", "English", "CS"]
marks = [80,75,90,85]
Requirements:
•	Add title
•	Add axis labels
'''
subjects = np.array(["Math", "Science", "English", "CS"])
marks = np.array([80, 75, 90, 85])
plt.bar(subjects, marks)
plt.title("Task 3: Bar Chart")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

'''
Task 5: Scatter Plot
Create scatter plot:
height = [150,160,165,170,175,180]
weight = [50,55,60,65,70,75]
Requirements:
•	Add title
'''
height = np.array([150,160,165,170,175,180])
weight = np.array([50,55,60,65,70,75])
plt.scatter(height, weight)
plt.title("Task 5: Scatter Plot")
plt.show()

'''
Task 6: Histogram
Create histogram for:
marks = [55,60,65,70,75,80,85,90,95,60,70,80]
Requirements:
•	Add title
'''
marks = np.array([55,60,65,70,75,80,85,90,95,60,70,80])
plt.hist(marks)
plt.title("Task 6: Histogram")
plt.show()

'''
Task 7: Pie Chart
Create pie chart:
languages = ["Python", "Java", "C++", "JavaScript"]
students = [40,25,20,15]
Requirements:
•	Explode
•	Shadow
'''
languages = np.array(["Python", "Java", "C++", "JavaScript"])
students = np.array([40, 25, 20, 15])
e = [0.2, 0, 0.1, 0]
plt.pie(students, labels=languages, explode=e, shadow=True)
plt.title("Task 7: Pie Chart")
plt.show()

'''
Task 8: Customize Plot (Using Numpy)
Create line plot with:
•	Marker
•	Linestyle
•	Color
'''
x = np.random.randint(100, size = (100))
y = np.random.randint(100, size = (100))
plt.plot(x, y, 'b:*')
plt.plot(x, y, "c")
plt.title("Task 8: Customize Plot (Using Numpy)")
plt.show()

'''
Task 9: Plot Sales Data
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [200,300,250,400,350]
Requirements:
•	Line plot
•	Marker
•	Title
'''
months = np.array(["Jan", "Feb", "Mar", "Apr", "May"])
sales = np.array([200, 300, 250, 400, 350])
plt.plot(months, sales, 'rp--')
plt.title("Monthly Sales")
plt.show()

