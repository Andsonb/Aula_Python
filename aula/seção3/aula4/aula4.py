#não podemos modificar uma tuple


t1= (1,2,3,4,5,6,'anderson')

print(type(t1))

t1=list(t1)

print(type(t1))

t1[2]=123

print(t1)
