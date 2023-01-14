#parameters when you a defining the funcition
#argument is when you use the function and pass the value

#positional parameters

def contact_card(name,age,car_model):
    return f"{name} is {age} and drives a {car_model}"

print(contact_card("Keith",29,"Honda Civic"))

#key word arguments
con=contact_card(age=29,car_model="Honda Civic",name="Keith")

print(con)

con=contact_card("Keith",car_model="Honda Civic",age=29)

print(con)
#when you start with key argument you can't change to positional
#con=contact_card(name="Keith","Honda Civic",age=29)

#don't need to specify the default parameter...when you call the function 
def can_drive(age, driving_age=16):
    return age >= driving_age

print(can_drive(29))
print(can_drive(16,18))

drive = can_drive(16,driving_age=18)
print(drive)

#when you define a default, everything after the default paramater must also be a default parameter..
#the below example doesnt work

#def can_drive(age, driving_age=16, vehicle_type):
#    pass

#this work
def can_drive(age, driving_age=16, vehicle_type='Totota'):
    return f"{age}, driving age >={driving_age}, vehicle type = {vehicle_type}"

print(can_drive(66))

#f(n) = f(n -2) + f(n -1)
