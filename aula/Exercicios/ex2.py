pergunta=input('digite a horas (0 a 23: ')

if pergunta.isdigit():
    pergunta=int(pergunta)
    if pergunta <= 0 or pergunta <=11:
        print('Bom dia {}'.format(pergunta))

    elif pergunta <= 12 or pergunta <=17:
        print('Boa tarde {}'.format(pergunta))

    elif pergunta <= 18 or pergunta <= 23:
        print('Boa Noite {}'.format(pergunta))
else:
    print('So aceitamos numero')