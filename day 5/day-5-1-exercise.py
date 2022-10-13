# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  print(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
#print(student_heights)

sum = int(0)
size = len(student_heights)
for h in student_heights:
    sum += int(h)
#avg = round(sum / size)
#print(avg)

n_students = int(0)
for n in student_heights:
    n_students += 1

avg = round(sum / n_students)    
print(avg)
    
    
    

    