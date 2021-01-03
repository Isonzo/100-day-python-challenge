student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

number_of_students = 0

height_total = 0

for student in student_heights:
    number_of_students += 1
    height_total += student

average = round(height_total / number_of_students, 2)

average = "{:.2f}".format(average)

print(average)
