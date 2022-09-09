from dados import produtos, pessoas, lista


def novalista(p):
    if p['preco'] > 12:
        return True


nova_lista = filter(novalista, produtos)

for list in nova_lista:
    print(list)
