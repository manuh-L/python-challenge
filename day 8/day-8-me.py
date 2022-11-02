# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("hello", end=" ")
    print("Good",end=" ")
    print("Morning")

greet()

#F allow input

def greet_with_name(name):
    print("hello",name, end=" ")
    print("Good",end=" ")
    print("Morning")

greet_with_name("Manuel")


#F with more than 1 input

def greet_with(name,location):
    print("hello",name, end=" ")
    print("Good",end=" ")
    print("Morning,")
    print(f"what is it like in {location}","?")
    


greet_with("Rock","Halifax")


# parameters is the name of the variable under the function greet(name)
#Argument is the value assigned to the parameter, e.g greet("manuel") .... name = "manuel"
#positional Arguments parametring .. default way of calling function


#keyword argument, the order of parameter doesn't matter, the argument is binded

#keyword arguments
greet_with(location="Halifax", name = "Rock")
