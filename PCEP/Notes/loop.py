

count = 0
while count < 10:
    if count % 2 ==0:
        count += 1
        continue
    print(f"we are counting odd numbers: {count}")
    count +=1


#break
count = 1
while count < 10:
    if count % 2 ==0:
        break
    print(f"we are counting odd numbers: {count}")
    count +=1

#break continue
colors = ['blue', 'green','red', 'white']
for color in colors:
    if color == 'blue':
        continue
    elif  color == 'red':
        break
    print(color)
    

#while else

count = 1
while count <=4:
    print(count)
    count +=1
else:
    print("while loop completed")
    

#for else
for i in [1,2,3,4,5]:
    print(i)
else:
    print("for loop completed")


colors = ['blue', 'green','red', 'white', 'orange']
for coloer in colors:
    if color == 'orange':
        print('orange is in the list')
        break
else:
    print("orange is not in the list")
    
#range
mr = range(10)
print(mr)
print(list(mr))


print(list(range(1,14,2)))


#list comprehensions
for _ in range(4):
    print('looping')
    
colors = ['blue', 'green','red', 'white', 'orange', 'purple']

up_c = []
for c in colors:
    up_c.append(c.upper())
print(up_c)

ti_c = [c.title() for c in colors]
print(ti_c)

warm_colors = [ color for color in colors  if color in ['red','orange','yellow']]
print(warm_colors)