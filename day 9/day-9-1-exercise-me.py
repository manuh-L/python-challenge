student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
student_grades = student_scores
for student in student_scores:
#    print(student_scores[student])
#    print(student)
#    student = "ola"
#    print(student)
    score = int(student_scores[student])
    if score <= 70:
        student_grades[student] = "Fail"
    elif score >= 71 and score <= 80:
        student_grades[student] = "Acceptable"
    elif score >= 81 and score <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif score <= 100 and score >= 91:
        student_grades[student] = "Outstanding"

#    print(student)
#    print(student_scores)

# 🚨 Don't change the code below 👇
print(student_grades)





