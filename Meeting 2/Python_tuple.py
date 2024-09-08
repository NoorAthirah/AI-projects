subjects =("Python","C++", "JavaScript")
# print(subjects)
# print(len(subjects))
      
print(subjects[-1]) #Display the last data
print(subjects[1])  #Display the second data
print(subjects[0:2]) #Display index 0 and index 1 (before index 2)
print("Python" in subjects)
print("Java" in subjects)

# subjects[1] = "C++" (error because values in tuples cannot change unlike list can add/delete value)
# print(subjects[1])

subject1, subject2,subject3 = subjects
print(subject1)
print(subject2)
print(subject3)
      
