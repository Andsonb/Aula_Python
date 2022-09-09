from dados import produtos, pessoas, lista


def aumenta_idade(p):
    p['nova_idade'] = round(p['preco'] * 1.20)
    return p


nomes = map(aumenta_idade, produtos)

for n in nomes:
    print(n)