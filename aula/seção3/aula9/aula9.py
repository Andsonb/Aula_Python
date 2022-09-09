from itertools import zip_longest, count

indece = count()
cidades = ['São paulo', 'belo horizonte','salvador', 'monte belo, outro']
estados = ['sp', 'mg', 'ba']


cidades_estados = zip(indece,cidades,estados)

for indece, v, i in cidades_estados:
    print(indece, v, i)

