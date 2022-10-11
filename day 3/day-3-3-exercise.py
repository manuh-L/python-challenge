# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? \n"))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print(f" The year {year} is a leap year")
else:
    print(f"{year} is not a leap year")