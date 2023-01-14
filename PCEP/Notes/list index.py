
mix = [1, "manuh", 2.0, 0b001]

print(mix)
print(mix[:2])

#invert lista
print(mix[::-1])

#even
print(mix[::2])

mix += ["dandy", 3.0]
print(mix)

mix[1:3] = ["replaced","rep"]
print(mix)

mix[3:4] = ["Lista","Creceu", "size", "mudou"]
print(mix)

#remove elements
mix[2:] = []
print(mix)

#remove 1st element
del mix[0]
print(mix)

#DELETE entire list
#del mix

#list function

#append -> at the end
mix.append("nhiuana")

print(mix)

#inset in positin
mix.insert(0,"novo")
print(mix)

#get index of alement
print(mix.index("novo"))

#check if element in the list
print("nhiuana" in mix)

print(0 not in mix)

print('a' in 'stargate')

#sort
print(sorted(mix))


#reverse
print(list(reversed(mix)))


##Nested list, Matrix

matrix = [[1,2,3], [4 ,5, 6]]

print(matrix)
row_count= len(matrix)
column_count = len(matrix[0])

print(matrix[0][1])