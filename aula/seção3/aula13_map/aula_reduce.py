from dados import produtos, pessoas, lista

from functools import reduce

soma_dos_produtos = reduce(lambda ac, a: ac + a['idade'], pessoas, 0)

print(soma_dos_produtos)
