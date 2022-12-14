#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6

#Format the result to 2 decimal places = 33.60

#Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Example Input
#Welcome to the tip calculator!
#What was the total bill? $124.56
#How much tip would you like to give? 10, 12, or 15? 12
#How many people to split the bill? 7
#Example Output
#Each person should pay: $19.93

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!\n")
bill = input("What was the total bill? $ ")
tip = input("How much tip would you like to give? ")
split = int(input("How many people to split the bill? "))

new_bill = float(bill)
new_tip = float(tip)
#new_split = int(split)

perc= (new_tip / 100) * new_bill
print(perc) 
perc += new_bill
print(perc) 

total = perc / split

total = round( total, 2)
new_total = "{:.2f}".format(total)
print(f"Each person should pay: ${new_total}")

