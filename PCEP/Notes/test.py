num = input("Enter a float value: ")
new_num = float(num) // 100 * 1.0
print(new_num)

#// retorna a parte interia 5 / 3 = 1... 1 / 100 = 0
#** exponecial, 2**3 = 8

#right operand of or is never evaluated
val = 1 or '2'
val *= 3
print(val)

#you can multiple string..output 222
print('2'*3)

#Expected Output:
False

values = ['Kevin Bacon', 60, '555-555-5555', False]
val = not values[1]
print(val)



ages = {'Keith': 30, 'Levi': 25, 'John': 20}
age = ages['Kevin'] ##error kevin doesnt exist and needs key:value.. example ages['Kevin'] = 12
print(ages * 2) ##error cant multiply dict

#correct
ages = {'Keith': 30, 'Levi': 25, 'John': 20}
ages['Kevin'] = 12
age = ages['Kevin'] 
print(ages)
print(age) #output 12



names = ['Alice', 'Bob', 'Lance', 'Mike']
all_names = names
names.remove('Bob') #bob is removed from both lists,
all_names + ['Kevin'] #Statement seems to have no effect, isn't assigned to any variable ou use append

#output
#['Alice', 'Lance', 'Mike']
#['Alice', 'Lance', 'Mike']

print(all_names + ['Kevin'] )
#['Alice', 'Lance', 'Mike', 'Kevin']


for num in range(10):
    print(num)
    if num % 2 == 0:
        continue
    else:
        break


def fib(n):
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
        yield a
fib_gen = fib(4)
print(fib_gen)


num = 15.1
num2 = num / 4
num2 //= 2
num2 + 1


for num in range(1, 10, 2):
    if num % 3:
        print(num)


num1 = 30
num2 = 15
num1 // 2
print(num2 == num1)

def double_values(list1):
    doubles = []
    for num in list1:
        doubles.append(str(num * 2))
    return doubles

first_list = [1, 2, 3, 4]
print(" ".join(double_values(first_list)))