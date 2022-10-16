#Step 1 

from operator import length_hint
import random


word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
list_size = len(word_list)
random_w = random.randint(0,list_size-1)


chosen_word = word_list[random_w]
print(chosen_word)

word_size = len(chosen_word)

x = ""

y =""

for character in range(0,word_size):
    x += "_ "

print(x)
print(word_size)
guess = input("guess a letter of the word\n").lower()


for letter in range(0,word_size):
    if chosen_word[letter] == guess:
        print("contains the letter:", guess)
        y += guess+" "
    
    else:
        y += "_ "

print(y)
#n = 0  
#while(n < word_size):
#
#    if chosen_word[n] == guess:
#        print("contains the letter", guess)
    
#    n += 1