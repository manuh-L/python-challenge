programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again.",
                          "loop": "The action of doing something over and over again"
                          }


print(programming_dictionary["Bug"])
print(programming_dictionary.items)

# adding item
programming_dictionary["Class"] = "File containing function and block of code"

print(programming_dictionary)

# initialize empty
emp_dic = {}

# edit value of a key
programming_dictionary["Bug"] = "error"

# loop through a dict
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


# wipe dict
programming_dictionary = {}


#nesting
capitais = {
    "Moz": "Maputo",
    "Portugal": "Lisboa" 
}


#newsting a list in a dict

travel_log = {
    "France": {"citties_visited": ["Paris","Lille","Dijon"], "total_vistis": 12},
    "USA": {"citties_visited": ["Miami","New York","Las Vegas"], "total_vistis": 50},
}


#nest dict in a list

travel_log = [
                {
                    "country": "France",
                    "citties_visited": ["Paris","Lille","Dijon"],
                    "total_vistis": 12 
                },
                {
                    "country": "USA", 
                    "citties_visited": ["Miami","New York","Las Vegas"],
                    "total_vistis": 50
                },
             ]