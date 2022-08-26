d1={
    'clientes': {'nome' : 'anderson',
                 'sobrenome': 'barbosa'},
    'clientes2': {'nome2' : 'dale',
                 'sobrenome': 'dely'}
   }

for i, e in d1.items():
    print(f'{i}')
    for a, w in e.items():
        print(f'{a} = {w}')