# dict, any mutable type
# each key must be unique...

ages = {"Manuel": 21, 'Dandy': 30}

# duplicated
ages = {"Manuel": 21, 'Dandy': 30}

print(ages)

#keys
for age in ages:
    print("keys: ",age)

#value
for age in ages:
    print("values",ages[age])
    
for name,age in ages.items():
    print(name,age)

# read
print(ages['Manuel'])
# print(ages.keys[21])


# assign
ages['Manuel'] = 10
ages['brown'] = 5
print(ages)

#delete
del ages['Manuel']
print(ages)

#check
print("brown" in ages)
print("Manuel" in ages)


#create dict

oi = dict(manuh=10, new1=110)
ola = dict([('manuh',10),('new1',110), ('Jr', 1)])

print(oi)
print(ola)

print(oi.values())
