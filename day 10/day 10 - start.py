

def format_name(f_name, l_name):
    """ Take the first and last name and return the first char
    in upper case"""
    if f_name == "" or l_name == "":
        return "empty"
#    f_name = input("first name\n")
#    l_name = input("last name\n")    

    ff_name = f_name.title()
    fl_name = l_name.title()
#    print(f_name,l_name)
    return f" result: {ff_name} {fl_name}"
    
name = format_name("manuel", "new1")
print(name)



