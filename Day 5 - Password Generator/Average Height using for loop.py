student_heights = input("Input list of student height: \n").split()
for n in range(0, len(student_heights)):
    student_heights[n]=int(student_heights[n])
print(student_heights)

total_height = 0
for height in student_heights:
    total_height += height

no_of_student = 0
for student in student_heights:
    no_of_student += 1

average_height = round(total_height / no_of_student)
print(average_height)
