
#get code poind for a char
print(ord('a'))
print(ord('b'))

print(id('a'))
print('')
print(id('a'))

#0x2122
#print(U+2122)
print(ord('\u2122'))

#code to symbol..
print('\u2122')
print(chr(8482))
#UTF8 - unicode transformation format, 8 bit length
#ASCII - letter number and comma pontuations... 


print("manuel".capitalize())
print("manuel eugenio nhiuana".title())

#all char can be represented as ascii?
print("manuel".isascii())

print("manuel".isspace())

print("manuel".isdecimal())

print("manuel".isdigit())

print("manuel".isnumeric())

print("manuel".isalpha())

print("manuel1".isalnum())

print("manuel".isidentifier())

print("manuel".isprintable())

#split
print("Manuel is a great pythonista".split())

url = "https://python.com/users/manuh"
words =url.split('/')
sword = "Manuh the goat".split()
user = url.split('/')[-1]
print(words)
print(user)

#join
print(", ".join(sword))

lines = ['First line', 'Second line', 'Third line']
output = "\n".join(lines)
print(output)

#format

form= "Hello, my name is {}, and I really enjoy {}, have a nice day!"
print(form.format('Manuel', 'Python'))

#disregard the 3 word
print(form.format('Manuel', 'Python', 'False'))

#error, not enough... tuple
#print(form.format('Manuel'))

#argument
warg= "Hello, my name is {0}, and I really enjoy {1}, have a nice day!\n {0}"
#warg= "Hello, my name is {0}, and I really enjoy {1}, have a nice day!\n {0}".format('Manuh', 'SRE')
#print(warg)
print(warg.format('Manuel', 'Python'))

name = input ("Your name?\n")

#be aware of the order, order matters, first hit and stops
if len(name) > 7:
    print("Ur name is long")
    
elif len(name) == 5:
    print("ur name is 5 characters")
    
elif len(name) >=4:
    print("ur name is 4 characters")
else:
    print("ur name is short")
    

#Pass....not doing
if name == "manuh":
    print("viva")
else:
    pass