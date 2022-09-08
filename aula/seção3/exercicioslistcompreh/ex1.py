

carrinho=[]

carrinho.append(('produto 1', 30))
carrinho.append(('produto 2', 20))
carrinho.append(('produto 3', 50))

#sum faz a soma
total=[]
preco=sum([float(y) for x, y in carrinho])

print(preco)