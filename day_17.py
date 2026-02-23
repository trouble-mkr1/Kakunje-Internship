print("sets: ")

course = {"python", "java", "C", "data science", "AIML"}

print(course, "\n")

new_course = {"cyber security", "cloud"}

print("union of the sets: ")
print(course.union(new_course), "\n")

print("difference of the sets: ")
print(course.difference(new_course), "\n")

new_course.clear()
print("cleared set: ")
print(new_course)
