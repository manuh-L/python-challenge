# Split string method
from random import randint
import random


names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

print(names)
print(len(names))
print(names[randint(0,len(names) - 1)])

#or
print(random.choice(names))