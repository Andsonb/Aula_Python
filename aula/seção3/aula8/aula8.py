lista= (1,2,3,4,5)

lista=iter(lista)
print(type(lista))

print(next(lista))

for i in lista:
    print(i)