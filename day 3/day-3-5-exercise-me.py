# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_lower = name1.lower()
name2_lower = name2.lower()

true = int(0)
love = int(0)

######TRUE########
true +=name1_lower.count("t")
true +=name1_lower.count("r")
true +=name1_lower.count("u")
true +=name1_lower.count("e")

true +=name2_lower.count("t")
true +=name2_lower.count("r")
true +=name2_lower.count("u")
true +=name2_lower.count("e")
print(f"for word true {true}")

######LOVE########
love +=name1_lower.count("l")
love +=name1_lower.count("o")
love +=name1_lower.count("v")
love +=name1_lower.count("e")

love +=name2_lower.count("l")
love +=name2_lower.count("o")
love +=name2_lower.count("v")
love +=name2_lower.count("e")
print(f"For word love {love}")

score = str(true) + str(love)
print(score)
love_score = int(score)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 39 and love_score < 51:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
 