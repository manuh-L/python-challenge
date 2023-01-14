users = ['Manuel', 'Dandy', 'Marley', 'Brown', 'Poly', 'bob','New1']
print(users)
print(users.index('bob'))

#users.remove('bob')
#users.pop(users.index('bob'))
del users[users.index('bob')]

print(users)

rev_users = users[::-1]
#or
rev_users1 = list(reversed(users))

print(rev_users)
print(rev_users1)


users.append('melody')
print(users)
#or
users += ["melody"]
print(users)

#slice to return 3 & 4 elements
print(users[2:4])
