# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#BMI = weight(kg)/ height^2(m2)
BMI = round(weight/ height**2)
if BMI < 18.5:
    print("underweight")
elif BMI < 25:
    print("normal weight")
elif BMI < 30:
    print("overweight")
elif BMI < 35:
    print("obese")
else:
    print("clinically obese")

#print(int(BMI))
