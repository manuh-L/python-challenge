from random import random
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print(paper)

choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

comp = random.randint(0,2)
print(comp)
op = [rock,paper,scissors]
#game = [op,num]

op[comp]

if(choose == comp):
    print(f'{op[choose]}\n')
    print(f"computer chose: \n {op[comp]}")
    print("DRAW")
elif(choose == 0 and comp == 1 or  choose == 1 and comp == 2 or choose == 2 and comp == 0):
    print(f'{op[choose]}\n')
    print(f"computer chose: \n {op[comp]}")
    print("You Lose")

elif(choose == 0 and comp == 2 or choose == 1 and comp == 0 or choose == 2 and comp == 1):
    print(f'{op[choose]}\n')
    print(f"computer chose: \n {op[comp]}")
    print("you Win")  

else:
    print(f"invalid option")
