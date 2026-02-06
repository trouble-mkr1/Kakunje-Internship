'''
task 1: Given Tuples: t1= (10, 20, "Python", "Code"), t2 = ("A", "B") 

1. Access and print the first element of t1. 
2. Access and print the last element of t2. 
3. Convert t1 into a list, change "Code" to "Program", and convert it back into a tuple. 
4. Unpack all elements of t1 into separate variables and print them. 
5. Join tl and t2 and store the result in a new tuple. 
6. Access elements from index 1 to 3 of the joined tuple.

Multiply the tuple t1 by 3 and print the result. t1 - (1, 2, 3) 
'''
t1= (10, 20, "Python", "Code")
t2 = ("A", "B")
print("task 1 output\n")

print(t1[0])
print(t2[-1])
l = list(t1)
l[3] = "Program"
t1 = tuple(l)
print(t1)
a, b, c, d = t1
print(a, b, c, d)
t3 = t1 + t2
print(t3)
print(t3[1:4])
t1 = (1, 2, 3)
print(t1 * 3)

print("==============================================================================================")
##########################################################################################################################
##########################################################################################################################
'''
task 2: my_set ={10, 20, 30, 40} 
1. Print the given set. 
2. Check whether 20 is present in my_set. 
3. Find and print the length of my_set. 
4. Add 50 to my_set. 
5. Remove 30 from my_set. 
6. Remove an element using discard() and note the output.
7. Remove a random element from my_set. 
8. Loop through my_set and print each element. 
9. Clear all elements from my_set. 

set1 = {1, 2, 3} 
set2 = {3, 4, 5, 6} 
10. Print the elements that are in set1 but not in set2. 
11. Print the elements that are in either set1 or set2 but not in both (symmetric difference). 
12. Add all items from set2 into set1 and print the updated set1. 
13. Print all unique elements from both set1 and set2. 
14. Add 7 to set1 and print the set. 
'''
my_set = {10, 20, 30, 40}
print("task 2 output\n")

print(my_set)
print(20 in my_set)
print(len(my_set))
my_set.add(50)
print(my_set)
my_set.remove(30)
print(my_set)
my_set.discard(60) # no error
print(my_set)
my_set.pop() # removing a random element
print(my_set)
for element in my_set:
    print(element)
my_set.clear()
print(my_set)

set1 = {1, 2, 3}
set2 = {3, 4, 5, 6}
print(set1 - set2)
print(set1.symmetric_difference(set2))
set1.update(set2)
print(set1)
print(set1.union(set2))
set1.add(7)
print(set1)

print("==============================================================================================")
##########################################################################################################################
##########################################################################################################################
'''
task 3: Given Dictionary: 
                        student ={ 
                            "name": "Anu", 
                            "age": 20, 
                            "course": "Python"
                        }
1. Print all keys, values, and all items in the dictionary. 
2. Access the value of "name". 
3. Access the value of "course" using get(). 
4. Add a new key "marks" with value 85. 
5. Update the value of "age" to 21. 
6. Remove "course" using pop(). 
7. Remove the last inserted item using popitem(). 
8. Loop through the dictionary and print keys and values.

students ={ 
"student1": {"name": "Anu", "age": 20}, 
"student2": {"name": "Ravi", "age": 21} 
9. Print the complete nested dictionary. 
10. Create a copy of the students dictionary

employee = { 
"emp_ id": 101, 
"name": "Kiran", 
"department": "HR", 
"salary": 35000 
13. Display all keys in the employee dictionary. 
14. Display all values in the employee dictionary. 
15. Display all key-value pairs (items) from the dictionary. 
16. Access and print the value of "name". 
17. Update the "salary" to 40000. 
'''
student ={
    "name": "Anu",
    "age": 20,
    "course": "Python"
}
print("task 3 output\n")

print(student.keys())
print(student.values())
print(student.items())
print(student["name"])
print(student.get("course"))
student["marks"] = 85
print(student)
student["age"] = 21
print(student)
student.pop("course")
print(student)
student.popitem()
print(student)
for key, value in student.items():
    print(f"{key}: {value}")

students = {
    "student1": {"name": "Anu", "age": 20},
    "student2": {"name": "Ravi", "age": 21}
}
print(students)
students_copy = students.copy()
print(students_copy)

employee = {
    "emp_id": 101,
    "name": "Kiran",
    "department": "HR",
    "salary": 35000
}
print(employee.keys())
print(employee.values())
print(employee.items())
print(employee["name"])
employee["salary"] = 40000
print(employee)

print("==============================================================================================")
##########################################################################################################################
##########################################################################################################################
