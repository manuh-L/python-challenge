
#string * repete x vezes a string, + concatena
rep = "helo " * 3
print(rep)


#binary

b = 0b10
a= 432
conv = bin(a)
print(b)
print(conv)
print(oct(a))
print(hex(a))

#retornar parte decimal
s = 3 // 2
print(s)

#unary, representar numero negativo '~'
#formula: -1 * a -1
aa=0b10
print(~aa)

 
#AND OR XOR NOT
xx = 0b0001
yy = 0b1100
#OR = | compara cada bit, 1 = true, 0 = false....1 or 0 = 1, 0 or 0 = 0, 1 or 1 = 1 
print(bin(xx | yy))

#END = & both of them must be true, 1 & 1 = 1, 1 & 0 = 0, 0 & 0 = 0
print(bin(xx & yy))

#?? duvida
#XOR exclusive OR, , 1 ^ 0 = 1, 0 ^ 0 = 0, 1 ^ 1= 0, 0 ^ 1 = 1
print(bin(xx ^ yy))

z = 0b1101
w = 0b1100
print(bin(z ^ w))


#shift operator, trunk digits
t = 0b110
print(t >> 2)

print(t >> 4)

#trunk 0, depois faz o calculo 0011, = 3
tt = 0b000000110
print(tt >> 1)

#add zeros 0 to the right
ss = 0b110
print(ss)
print(ss << 2)
print(bin(ss << 2))

#return oposite
# not true, return false
#not False, return true


print(False or False) #false
print(False and False) #False
print(False and True) #false
print(False or True) #true


print("#comparison")
print('a' > 'a') #false
print('a' < 'b') #true
print('a' > 'b') #false

print('bb' > 'aa') #true
print('ab' > 'ba' ) #false
print('bb' <= 'ba') #false

#ver value
print(ord('a'))

#Caracter mais tem valor diff A
print(ord('A'))

print('A' >= 'a') #false

# iguais ou equivalentes ==
print( 5 == 5) #true

print('b' == 'b') #true

print('a' != 'a' ) #false

print('b' != 'w') # true

print('a' == 1) #false

#is not is

print(1 is 1)#true int is imutable, you cant change
print('a' is 1) #false

print([] is []) #false lists a mutable

print('a' is 'a') #true string is also imu..

print('a' is not a) #false

#check imutability 
print(id('a'))
print(id(1))
print(id('a'))

# a is a 'e similar
print(id('a') == id('a'))

print([1, 2] is [1, 2]) #false


#operator priority
#criacao de listas [] ou dict {}, tem prioridade.. sao criados antes de qualquer operacao
#function no meio de algo ou uma expresao, a funcao e executada primeiro
# +1, -1, ~1
#**, *, /

#typecast
print(int(1.2))
#print(int('1.2')) #error
print(str(1))

print(bool(1)) #true
print(bool('Dandy')) #true

print(bool(0.0))
print(1 and 0) #0 false?

print(1 and 1) # true return 1

print('this' and 'that') #false return that.. and return false value

print(0 and 1) # return 0

print(0 or 1) #return 1

print(not "")

print(not 1) #false

##INPUT
name = input("what is yout name: ")
age = int(input("yout age: "))


#print por default multiplas linhas print, imprime cada linha 1 print -> 1 line, new line
#sep = separator
#end = ditar o que acontece no final de cada linha print

print("manuh", end=" ")
print("is my name", end=" ")

print(name,'Tenho',age,'anos','cor preferida,natural de tete.',sep=" ")
print(name,'Tenho',age,'anos', 'cor preferida,natural de tete.',sep=",")
