# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

col= int(position[0])
row = int(position[1])
print(col,row)

#row1[col-1] = "X"
#row1[row-1] = row
#print(row1)
#print(f"{row1}\n{row2}\n{row3}")
if(row == 1):
    row1[col-1] = "X"
elif (row == 2):
    row2[col-1] = "X"
elif (row == 3):
    row3[col-1] = "X"
else:
    print("error out of bound")

print(f"{row1}\n{row2}\n{row3}")


#31
#o primeiro digito esolhe o elemento ou posicao, e o ultimo escolhe a lista
#element 1 of row 3
