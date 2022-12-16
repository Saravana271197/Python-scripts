students_enrolled = ["Michael", "Jack", "Jill", "Nathan"]
student_count = students_enrolled.count("Jack")
print(student_count)

student_index = students_enrolled.index("Michael")
print(student_index)
#index method shows the index position number of the given item
students_enrolled.reverse()
#reverse method reverses the list
print(students_enrolled)
students_enrolled.append("Ron")
print(students_enrolled)
#append method appends an item to the list in the last place
students_enrolled.sort()
#Sort method sorts the list in alphabetical order
print(students_enrolled)
student_poped = students_enrolled.pop()
#pop mthod removes the last item in the list
print(student_poped)
