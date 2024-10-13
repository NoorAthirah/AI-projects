# allowance = 10
# spending = 8
# print(allowance < spending)
# print(allowance > spending)
# print(allowance != spending)
# print(allowance == spending)

# print((allowance == 10) and (spending == 8)) #True
# print((allowance == 12) or (spending == 8)) #True

students_name = ['Alex','Bryan','Christ','Dave','Eva']
students_score = [100,75,80,78,99]
students_grade = [] # <-- Akan berisi grade dari masing-masing siswa

for i in students_score:
    if ( i >= 90):
        students_grade.append('A') # Add values ​​to the list.
    elif(i >= 70):
        students_grade.append('B')
    else:
        students_grade.append('C') 
print(students_grade)