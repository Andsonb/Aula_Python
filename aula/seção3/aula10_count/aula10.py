from itertools import count

contador = count(start=0, step=1)

#for i in contador:
#   print(i)

#    if i >= 10:
#        break


nomes_com_id = ['anderson', 'barbosa', 'da silva']
juntando_id = zip(contador, nomes_com_id)

for i, b in juntando_id:
    print(i, b)
