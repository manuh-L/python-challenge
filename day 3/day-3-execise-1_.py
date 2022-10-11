print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? \n"))

if height > 120:
  print("You can Ride!")
  age=int(input("what is your age? \n"))
  if age < 12:
      print("Pay $5")
  elif age <= 18:
      print("Pay $7")
  elif age <= 50:
      print("Pay $12")
  else:
      print("Free!")
else:
  print("Sorry, Grow up!! you are't taller")  