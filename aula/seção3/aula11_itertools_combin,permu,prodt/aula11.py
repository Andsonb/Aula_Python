"""
combinations, permutations e product - Itertools
combinação - ordem não importa
permutação - ordem importa
ambos não repetem valores unicos

produto - ordem importa e repete valores unicos

"""

from itertools import combinations, permutations, product

pessoas = ['anderson', 'luiz', 'paulo', 'marks']

for grupo in product(pessoas, repeat=2):
    print(grupo)
