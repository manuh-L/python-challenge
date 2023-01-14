

The way in which we are passing the arguments into the print() function is the most common in Python, and is called the positional way (this name comes from the fact that the meaning of the argument is dictated by its position,
e.g., the second argument will be outputted after the first, not the other way round).


The mechanism is called keyword arguments. The name stems from the fact that the meaning of these arguments is taken not from its location (position) but from the special word (keyword) used to identify them.

The print() function has two keyword arguments that you can use for your purposes. The first of them is named end.

In the editor window you can see a very simple example of using a keyword argument.

In order to use it, it is necessary to know some rules:

a keyword argument consists of three elements: a keyword identifying the argument (end here); an equal sign (=); and a value assigned to that argument;
any keyword arguments have to be put after the last positional argument (this is very important)

e.g
print("My name is", "Python.", end=" ")
print("Monty Python.")

As you can see, the end keyword argument determines the characters the print() function sends to the output once it reaches the end of its positional arguments.

The default behavior reflects the situation where the end keyword argument is implicitly used in the following way: end="\n".


#sep
We've said previously that the print() function separates its outputted arguments with spaces. This behavior can be changed, 
too.

The keyword argument that can do this is named sep (like separator).

The sep argument delivers the following results:

print("My", "name", "is", "Monty", "Python.", sep="-")

Both keyword arguments may be mixed in one invocation, just like here in the editor window.

print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")


#exercise
Modify the first line of code in the editor, 
using the sep and end keywords, to match the expected output. Use the two print() functions in the editor.
Expected output
Programming***Essentials***in...Python

print("Programming","Essentials","in", sep="***",end="...")
print("Python")


print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

Try to:

minimize the number of print() function invocations by inserting the \n sequence into the strings
make the arrow twice as large (but keep the proportions)
duplicate the arrow, placing both arrows side by side; note: a string may be multiplied by using the following trick: "string" * 2 will produce "stringstring" (we'll tell you more about it soon)
remove any of the quotes, and look carefully at Python's response; pay attention to where Python sees an error - is this the place where the error really exists?
do the same with some of the parentheses;
change any of the print words into something else, differing only in case (e.g., Print) - what happens now?
replace some of the quotes with apostrophes; watch what happens carefully.

print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print(' ','*'*5)


 In Python strings the backslash (\) is a special character which announces that the next character has a different meaning, e.g., \n (the newline character) starts a new output line.

7. Positional arguments are the ones whose meaning is dictated by their position, e.g., the second argument is outputted after the first, the third is outputted after the second, etc.

8. Keyword arguments are the ones whose meaning is not dictated by their location, but by a special word (keyword) used to identify them.


#literals
Therefore, you can write this number either like this: 11111111, or like that: 11_111_111.

And how do we code negative numbers in Python? As usual - by adding a minus. You can write: -11111111, or -11_111_111.

Positive numbers do not need to be preceded by the plus sign, but it's permissible, if you wish to do it. The following lines describe the same number: +11111111 and 11111111.

print(0o123) #octal
print(0x123) #hexa
print(0b10) #bin
print(101_111_000)


In essence, you can write the value 0.4 as:
.4

For example: the value of 4.0 could be written as:

4.


Take, for example, the speed of light, expressed in meters per second. Written directly it would look like this: 300000000.

To avoid writing out so many zeros, physics textbooks use an abbreviated form, which you have probably already seen: 3 x 108.

In Python, the same effect is achieved in a slightly different way - take a look:

3E8

The letter E (you can also use the lower-case letter e - it comes from the word exponent) is a concise record of the phrase times ten to the power of.

Note:

the exponent (the value after the E) has to be an integer;
the base (the value in front of the E) may be an integer.



A physical constant called Planck's constant (and denoted as h), according to the textbooks, has the value of: 6.62607 x 10-34.

6.62607E-34
For example, let's say you've decided to use the following float literal:

0.0000000000000000000001
print(0.0000000000000000000001)
this is the result:

1e-22
Python always chooses the more economical form of the number's presentation,
 and you should take this into consideration when creating literals.

 print("I like \"Monty Python\"")
 print('I like "Monty Python"')

print('I\'m Monty Python.')
print("I'm Monty Python.")

#true =1
#false = 0

print(True > False)
print(True < False)


print("I'm\n\"\"learning\"\"\n\"\"\"python\"\"\"")

#op

A ** (double asterisk) sign is an exponentiation (power) operator. Its left argument is the base, its right, the exponent.
Classical mathematics prefers notation with superscripts, just like this: 23. 
Pure text editors don't accept that, so Python uses ** instead, e.g., 2 ** 3.

Note: we've surrounded the double asterisks with spaces in our examples.
 It's not compulsory, but it improves the readability of the code.
print(2 ** 3) #8
print(2 ** 3.) #8.0
print(2. ** 3) #8.0
print(2. ** 3.) #8.0



The result produced by the division operator is always a float, regardless of whether 
or not the result seems to be a float at first glance: 1 / 2, or if it looks like a pure integer: 2 / 1.

A // (double slash) sign is an integer divisional operator. It differs from the standard / operator in two details:

its result lacks the fractional part - it's absent (for integers), or is always equal to zero (for floats); 
this means that the results are always rounded;
it conforms to the integer vs. float rule.

print(6 // 3) #2
print(6 // 3.) #2.0
print(6. // 3) #2.0
print(6. // 3.) #2.0

The result of integer division is always rounded to the nearest integer value that is less than the real (not rounded) result.

This is very important: rounding always goes to the lesser integer.


print(-6 // 4) #-2
print(6. // -4) #-2
pk resultado -1.5 e menor numero inteiro proximp de -1.5 e' 2.0

Note: some of the values are negative. This will obviously affect the result. But how?


The result is two negative twos. The real (not rounded) result is -1.5 in both cases. However, 
the results are the subjects of rounding. 
The rounding goes toward the lesser integer value, and the lesser integer value is -2, hence: -2 and -2.0.

Integer division can also be called floor division. You will definitely come across this term in the future.

#Operators: remainder (modulo)
The next operator is quite a peculiar one, because it has no equivalent among traditional arithmetic operators.

Its graphical representation in Python is the % (percent) sign, which may look a bit confusing.

Try to think of it as of a slash (division operator) accompanied by two funny little circles.

The result of the operator is a remainder left after the integer division.

In other words, it's the value left over after dividing one value by another to produce an integer quotient.

Note: the operator is sometimes called modulo in other programming languages.

Take a look at the snippet - try to predict its result and then run it:

print(14 % 4)

As you can see, the result is two. This is why:

14 // 4 gives 3 → this is the integer quotient;
3 * 4 gives 12 → as a result of quotient and divisor multiplication;
14 - 12 gives 2 → this is the remainder.


Operators and their bindings
The binding of the operator determines the order of computations performed by some operators with equal priority, 
put side by side in one expression.

Most of Python's operators have left-sided binding, which means that the calculation of the expression is conducted from left to right.

This simple example will show you how it works. Take a look:
print(9 % 6 % 2)
There are two possible ways of evaluating this expression:

from left to right: first 9 % 6 gives 3, and then 3 % 2 gives 1;
from right to left: first 6 % 2 gives 0, and then 9 % 0 causes a fatal error.

#Operators and their bindings: exponentiation
print(2 ** 2 ** 3)
2 ** 3 → 8; 2 ** 8 → 256
The result clearly shows that the exponentiation operator uses right-sided binding.

print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

#Keywords
'False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']




# If you'd like to quickly comment or uncomment multiple lines of code, select the line(s) you wish to modify and use the following keyboard shortcut: CTRL + / (Windows) or CMD + / (Mac OS). It's a very useful trick, isn't it? Try this code in Sandbox.


#
Replication
The * (asterisk) sign, when applied to a string and number (or a number and string, as it remains commutative in this position) becomes a replication operator:


Priority	Operator	
1	+, -	unary
2	**	
3	*, /, //, %	
4	+, -	binary
5	<, <=, >, >=	
6	==, !=


#x, y, z = 5, 10, 8