for num in range(10):
    print(num)
    if num % 2 == 0:
        continue
    else:
        break
    
doubles =[]

print("1600 Pennsylvania Ave NW", "Washington", "DC", sep=',')


pair1 = ('a', 'b', 'c')
pair2 = ('d', 'e', 'f')
index = 0

while index < len(pair1):
    for item in pair2:
        print(pair2[index], item)
    index += 1
    
    

def fib(n):
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
        yield a
fib_gen = fib(4)
print(fib_gen)

#The yield statement within the function 
#body shows that we're creating a generator, so we won't see the values until we call next(fib_gen).


def double_values(list1):
    doubles = []
    for num in list1:
        doubles.append(str(num * 2))
    return doubles

first_list = [1, 2, 3, 4]
print(" ".join(double_values(first_list)))


def f(x):
    if x ==0:
        return 0
    else:
        return f(x-1) + 1
    
print(f(3))


for num in range(10):
    print(num)
    if num % 2 == 0:
        continue
    else:
        break
    
ages = {'Keith': 30, 'Levi': 25, 'John': 20}
output = list(ages.keys())
print(output)

#The keys method returns a list consisting of all of the keys from the dictionary.
# Furthermore, the list function is needed, otherwise the return value would be dict_keys(['Keith', 'John', 'Levi']) .

ages = {'Keith': 30, 'Levi': 25, 'John': 20}
output = [str(value) for value in ages.values()]
print(output)




a =  bin(2) and bin(0)
#The and operator is used to evaluate the truth value of the expression '0b10' and '0b0'. 
#Since both operands are non-empty strings, they are considered to be true.
#The and operator returns the last operand if both operands are true, so the result of the expression is '0b0'.

# 0 = false.. and e' usado para analisar se o valor e' true... qualquer valor comparado com 0 vai ser 0, isto e' = FALSE
#caso nao, AND retorna o right value do lado do AND

#The and operator is used to evaluate the truth value of the expression 0 and 1. Since the first operand is 0, it is considered to be false.
#The and operator returns the first operand if either of the operands is false, so the result of the expression is 0.

#^
# 2 ^ 3 = 1?


txt = 'manuel'

print(txt[0::2])

#reverse
print(txt[::-1])