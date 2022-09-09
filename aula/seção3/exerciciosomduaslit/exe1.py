lista = [1, 2, 3, 4, 5, 6, 7]
lista2 = [1, 2, 3, 4]

somalist = [x + y for x, y in zip(lista, lista2)]

print(somalist)
