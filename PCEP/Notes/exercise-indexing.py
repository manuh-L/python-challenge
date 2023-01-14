
string = input("insert the string")

string_length = len(string)

print("First character is :",string[0])
print("Last character is :",string[-1])
print("Middle character is :",string[round(((string_length-1)/2))])
print("Even characters are :",string[::2])
print("Odd characters are :",string[1::2])
print("String in reverse :",string[::-1])
